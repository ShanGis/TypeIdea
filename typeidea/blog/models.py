from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    STATUS_ITEMS = (
        (1, '正常'),
        (2, '删除'),
    )
    
    name = models.CharField(max_length=50, verbose_name='名称')
    status = models.PositiveIntegerField(default=1, choices=STATUS_ITEMS, verbose_name='状态')
    is_nav = models.BooleanField(default=False, verbose_name='是否置顶导航')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    
    class Meta():
        verbose_name = verbose_name_plural = '分类'

    def __str__(self):
        return self.name


class Tag(models.Model):
    STATUS_ITEMS = (
        (1,'正常'),
        (2,'删除'),
    )

    name = models.CharField(max_length=50, verbose_name='名称')
    status = models.PositiveIntegerField(default=1, choices=STATUS_ITEMS, verbose_name='状态')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta():
        verbose_name = verbose_name_plural = '标签'

    def __str__(self):
        return self.name

class Post(models.Model):
    # title,dec,content,status,category,tag,owner,created_time
    STATUS_ITEMS = (
        (1, '正常'),
        (2, '删除'),
        (3, '草稿'),
    )

    title = models.CharField(max_length=255, verbose_name="标题")
    dec = models.CharField(max_length=1024, blank=True, verbose_name="摘要")
    status = models.PositiveIntegerField(default=1, choices=STATUS_ITEMS, verbose_name="状态")
    content = models.TextField(verbose_name="内容", help_text="正文必须为MarkDown格式")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="分类")
    tag = models.ManyToManyField(Tag, verbose_name="标签")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="作者")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta():
        verbose_name = verbose_name_plural = '文章'



