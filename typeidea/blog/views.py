from django.core.paginator import Paginator,EmptyPage
from django.shortcuts import render
from django.http import HttpResponse,Http404

from .models import Post, Category, Tag


def post_list(request, category_id=None, tag_id=None):
    queryset = Post.objects.all()

    page = request.GET.get('page', 1)
    page_size = 4
    try:
        page = int(page)
    except TypeError:
        page = 1

    if category_id:
        queryset = queryset.filter(category_id=category_id)
    elif tag_id:
        try:
            tag = Tag.objects.get(id=tag_id)
        except tag.DoesNotExist:
            queryset = []
        else:
            queryset = tag.posts.all()

    paginator = Paginator(queryset, page_size)
    try:
        posts = paginator.page(page)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
   

    context = {
        'posts': posts
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
