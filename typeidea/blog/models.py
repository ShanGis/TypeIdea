from django.contrib.auth.models import User
from django.db import models

import markdown

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
    is_markdown = models.BooleanField(verbose_name='使用MarkDown格式', default=True)
    html = models.TextField(verbose_name='内容HTML格式', null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="分类")
    tag = models.ManyToManyField(Tag, related_name='posts' ,verbose_name="标签")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="作者")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    # Model层定制字段
    def status_show(self):
        return '当前标状态:%s' % self.status
    status_show.short_description = '演示状态'

    def save(self, *args, **kwargs):
        if self.is_markdown:
            config = {
            'codehilite': {
                'use_pygments': False,
                'css_class': 'prettyprint linenums',
                }
            }
            self.html = markdown.markdown(self.content, extensions=['codehilite'], extension_configs=config)
        return super().save(*args, **kwargs)

    class Meta():
        verbose_name = verbose_name_plural = '文章'

    def __str__(self):
        return self.title



