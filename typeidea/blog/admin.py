from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Post, Category, Tag
from .adminforms import PostAdminForm
from typeidea.custom_site import post_admin_site
from typeidea.custom_admin import BaseOwnerAdmin
# from comment.admin import CommentInlineAdmin 


@admin.register(Post, site=post_admin_site)
class PostAdimn(BaseOwnerAdmin):
    form = PostAdminForm
    # 展示页面
    list_display = (
        'title', 'category', 'owner', 
        'created_time', 'status_show', 'operate',
    )
    # list_display_links = (
    #     # 'category',
    #     'title',
    # )

    list_filter = ['category', 'owner']
    # search_fields = ['title', 'category__name', 'status', 'owner__username']
    search_fields = ['title', 'category__name']
    # show_full_result_count = False

    actions_on_top = False
    actions_on_bottom = True

    date_hierarchy = 'created_time'
    # list_editable = ('category',)

    # 编辑页面
    save_on_top = False 
    fields = (
        ('title', 'category'),
        'dec',
        'status',
        'content',
        'tag',
    )
    # inlines = [CommentInlineAdmin]

    # Admin层自定义字段 
    def operate(self, obj):
        return format_html(
            "<a href='{}'>编辑</a>",
            reverse('post_admin:blog_post_change', args=(obj.id,))
        )
    operate.short_description = '操作'


class PostInLineAdimn(admin.TabularInline):
    fields = ('title', 'status')
    extra = 3
    model = Post

@admin.register(Category, site=post_admin_site)
class CategoryAdmin(BaseOwnerAdmin):
    # inlines = [PostInLineAdimn]
    list_display = ['name', 'status', 'is_nav', 'created_time']
    fields = (
        'name', 'status', 'is_nav',
    )


@admin.register(Tag, site=post_admin_site)
class TagAdmin(BaseOwnerAdmin):
    list_display = ['name', 'status', 'created_time']
