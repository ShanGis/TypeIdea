from django.contrib import admin
from django.urls import path

from .custom_site import post_admin_site, comment_admin_site, config_admin_site
from blog.views import (AuthorView, CategoryView, 
                        IndexView, TagView, PostView)
from config.views import links


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('post/<int:pk>/', PostView.as_view(), name='detail'),
    path('category/<int:category_id>/', CategoryView.as_view(), name='category'),
    path('tag/<int:tag_id>/', TagView.as_view(), name='tag'),
    path('author/<int:author_id>/', AuthorView.as_view(), name='author'),
    path('links/', links, name='links'),
    path('admin/', admin.site.urls),
    path('post_admin/', post_admin_site.urls),
    path('comment_admin/', comment_admin_site.urls),
    path('config_admin/', config_admin_site.urls)
]
