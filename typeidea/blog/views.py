from django.core.paginator import Paginator,EmptyPage
from django.shortcuts import render
from django.http import HttpResponse,Http404

from .models import Post, Category, Tag
from config.models import SideBar
from comment.models import Comment

def post_list(request, category_id=None, tag_id=None):
    queryset = Post.objects.all()
    
    # 分类、标签视图
    if category_id:
        queryset = queryset.filter(category_id=category_id)
    elif tag_id:
        try:
            tag = Tag.objects.get(id=tag_id)
        except tag.DoesNotExist:
            queryset = []
        else:
            queryset = tag.posts.all()
    
    # 分页
    page = request.GET.get('page', 1)
    page_size = 4
    try:
        page = int(page)
    except TypeError:
        page = 1
    paginator = Paginator(queryset, page_size)
    try:
        posts = paginator.page(page)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    
    # 分类导航
    cates = Category.objects.filter(status=1)
    nav_cates = []
    not_nav_cates = []
    for cate in cates:
        if cate.is_nav:
            nav_cates.append(cate)
        else:
            not_nav_cates.append(cate)
    
    # 侧边栏
    side_bars = SideBar.objects.filter(status=1)
    recently_posts = Post.objects.filter(status=1)[:10]
    recently_comments = Comment.objects.filter(status=1)[:10]



    # 模板内容
    context = {
        'posts': posts,
        'nav_cates': nav_cates,
        'not_nav_cates': not_nav_cates,
        'side_bars': side_bars,
        'recently_posts': recently_posts,
        'recently_comments': recently_comments,
    }
    return render(request, 'blog/list.html', context=context)

    

    

def post_detail(request, pk=None):
    try:
        queryset = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        raise Http404('好像没有你要找的文章呐')

    context = {
        'post': queryset
    }
    return render(request, 'blog/detail.html', context=context)
