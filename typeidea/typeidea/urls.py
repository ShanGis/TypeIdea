import xadmin
xadmin.autodiscover()
from xadmin.plugins import xversion
xversion.register_models() 
from ckeditor_uploader import urls as uploader_urls
from django.contrib import admin
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from rest_framework import routers
from rest_framework.documentation import include_docs_urls

from blog.views import (
    AuthorView, CategoryView, 
    IndexView, TagView, PostView
                        )
from config.views import LinkView
from comment.views import CommentView
from typeidea import adminx
from blog.api import PostViewSet, CategoryViewSet
from .autcomplete import CategoryAutoComplete,TagAutoComplete

router = routers.DefaultRouter()
router.register(r'post', PostViewSet)
router.register(r'category', CategoryViewSet)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('post/<int:pk>/', PostView.as_view(), name='detail'),
    path('category/<int:category_id>/', CategoryView.as_view(), name='category'),
    path('tag/<int:tag_id>/', TagView.as_view(), name='tag'),
    path('author/<int:author_id>/', AuthorView.as_view(), name='author'),
    path('links/', LinkView.as_view(), name='links'),
    path('comments/', CommentView.as_view(), name='comments'),
    path('admin/', xadmin.site.urls),
    path('category-autocomplete/', CategoryAutoComplete.as_view(), name='category-autocomplete'),
    path('tag-autocomplete/', TagAutoComplete.as_view(), name='tag-autocomplete'),
    url('ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^api/', include(router.urls)),
    url(r'^docs/', include_docs_urls(title='typeidea apis'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
