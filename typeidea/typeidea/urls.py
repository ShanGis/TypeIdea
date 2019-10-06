from django.contrib import admin
from django.urls import path

from .custom_site import post_admin_site, comment_admin_site, config_admin_site
from blog.views import post_list, post_detail
from config.views import links


urlpatterns = [
    path('', post_list, name='index'),
    # path('post/', post_detail),
    path('post/<int:pk>/', post_detail, name='detail'),
    path('category/<int:category_id>/', post_list, name='category'),
    path('tag/<int:tag_id>/', post_list, name='tag'),
    path('links/', links, name='links'),
    path('admin/', admin.site.urls),
    path('post_admin/', post_admin_site.urls),
    path('comment_admin/', comment_admin_site.urls),
    path('config_admin/', config_admin_site.urls)
]
