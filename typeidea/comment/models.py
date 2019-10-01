from django.db import models
from django.contrib.auth.models import User

from blog.models import Post


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='文章')
    content = models.CharField(max_length=2000, verbose_name='内容')
    nickname = models.CharField(max_length=50, verbose_name='别名')
    websit = models.URLField(verbose_name='网址')
    email = models.EmailField(verbose_name='邮箱')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class META():
        verbose_name = verbose_name_plural = '评论'