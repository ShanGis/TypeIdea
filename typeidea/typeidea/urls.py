import re

import xadmin
xadmin.autodiscover()
from xadmin.plugins import xversion
xversion.register_models() 
from ckeditor_uploader import urls as uploader_urls
from django.contrib import admin
from django.conf.urls import url, include
from django.views.static import serve
from django.conf import settings
from django.urls import path
from rest_framework import routers
from rest_framework.documentation import include_docs_urls

from blog.api import (
    CategoryViewSet, TagViewSet, PostViewSet, UserViewSet,
    )
from blog.views import (
    AuthorView, CategoryView, 
    IndexView, TagView, PostView
                        )
from config.views import LinkView
from comment.views import CommentView
from typeidea import adminx
from .autocomplete import CategoryAutocomplete, TagAutocomplete

router = routers.DefaultRouter()
router.register(r'post', PostViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'tag', TagViewSet)
router.register(r'user', UserViewSet)


def static(prefix, **kwargs):
    return [
        url(r'^%s(?P<path>.*)$' % re.escape(prefix.lstrip('/')), serve, kwargs=kwargs),
     ]

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('post/<int:pk>/', PostView.as_view(), name='detail'),
    path('category/<int:category_id>/', CategoryView.as_view(), name='category'),
    path('tag/<int:tag_id>/', TagView.as_view(), name='tag'),
    path('author/<int:author_id>/', AuthorView.as_view(), name='author'),
    path('links/', LinkView.as_view(), name='links'),
    path('comments/', CommentView.as_view(), name='comments'),
    path('admin/', xadmin.site.urls),
    url(r'^category-autocomplete/$', CategoryAutocomplete.as_view(), name='category-autocomplete'),
    url(r'^tag-autocomplete/$', TagAutocomplete.as_view(), name='tag-autocomplete'), 
    # path('category-autocomplete/', CategoryAutoComplete.as_view(),
    #      name='category-autocomplete'),
    # path('tag-autocomplete/', TagAutoComplete.as_view(), name='tag-autocomplete'),
    url('ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^api/', include(router.urls)),
    url(r'^docs/', include_docs_urls(title='typeidea apis'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
        # url(r'^silk/', include('silk.urls', namespace='silk')),
                   ] + urlpatterns
