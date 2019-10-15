import xadmin
xadmin.autodiscover()
from xadmin.plugins import xversion
xversion.register_models() 
from django.contrib import admin
from django.urls import path

from blog.views import (AuthorView, CategoryView, 
                        IndexView, TagView, PostView)
from config.views import LinkView
from comment.views import CommentView
from typeidea import adminx


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('post/<int:pk>/', PostView.as_view(), name='detail'),
    path('category/<int:category_id>/', CategoryView.as_view(), name='category'),
    path('tag/<int:tag_id>/', TagView.as_view(), name='tag'),
    path('author/<int:author_id>/', AuthorView.as_view(), name='author'),
    path('links/', LinkView.as_view(), name='links'),
    path('comments/', CommentView.as_view(), name='comments'),
    path('admin/', xadmin.site.urls),
]
