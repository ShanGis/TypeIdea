from django.db import models
from django.contrib.auth.models import User


class Link(models.Model):
    STATUS_ITEM = (
        (1, '正常'),
        (2, '删除'),
    )
    title = models.CharField(max_length=50, verbose_name='标题')
    href = models.URLField(verbose_name='链接')
    status = models.PositiveIntegerField(default=1, choices=STATUS_ITEM, verbose_name='状态')
    weight = models.PositiveIntegerField(default=1, choices=zip(range(1, 6), range(1, 6)),
                                        verbose_name='权重', 
                                        help_text='权重越高展示顺序越靠前')
    
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta():
        verbose_name = verbose_name_plural = '友链'

    def __str__(self):
        return self.title

    def status_show(self):
        return '当前状态{}'.format(self.status)
    status_show.short_description = '状态'


class SideBar(models.Model):
    STATUS_ITEM = (
        (1, '正常'),
        (2, '下线')
    )

    SIDE_TYPE = (
        (1, 'HTML'),
        (2, '最新文章'),
        (3, '最热文章'),
        (4, '最近评论'),
    )
    title = models.CharField(max_length=50, verbose_name="标题")
    display_type = models.PositiveIntegerField(default=1, choices=SIDE_TYPE, verbose_name='展示类型')
    content = models.CharField(max_length=500, blank=True, verbose_name='内容',
                                 help_text='如果设置的不是HTML类型，可为空') 

    status = models.PositiveIntegerField(default=1, choices=STATUS_ITEM, verbose_name='状态')  
    
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta():
        verbose_name = verbose_name_plural = '侧边栏'

    def status_show(self):
        return '当前状态{}'.format(self.status)
    status_show.short_description = '状态'
    
    def __str__(self):
        return self.title