from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
import xadmin

from .models import Comment
from .adminform import CommentAdminForms
from typeidea.adminx import BaseOwnerAdmin


class CommentAdmin(object):
    # 展示页面定制
    list_display = [
        'target', 'content', 'nickname_show',
        'email', 'created_time', 'open_comment_website'
    ]
    list_filter = ['nickname', 'target', 'created_time']
    search_fields = ['nickname', 'target']

    date_hierarchy = 'created_time'

    # 编辑页面定制
    form = CommentAdminForms
    save_on_top = False
    save_on_bottom = True
    fields = (
        'target',
        'nickname',
        'email',
        'content', 
        'websit'
    )
    

    def open_comment_website(self, obj):
        return format_html(
            '<a href={}>跳转至评论页</a>',
            reverse('comment_amdin:comment_comment_change', args=(obj.id,))
            )
    open_comment_website.short_description = '评论页'

xadmin.site.register(Comment, CommentAdmin)

# class CommentInlineAdmin(admin.TabularInline):
#     fields = ('nickname','content')
#     extra = 1
#     model = Comment
