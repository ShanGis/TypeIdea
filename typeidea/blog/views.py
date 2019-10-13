from django.core.cache import cache
from django.views.generic import ListView,DetailView

from .models import Post, Category, Tag
from comment.models import Comment
from comment.forms import CommentForms
from config.models import SideBar
from typeidea.common import CommonMixin,CommentMixIn


class BasesPostsView(CommonMixin, ListView):
    model = Post
    template_name = 'blog/list.html'
    context_object_name = 'posts'
    paginate_by = 3


class IndexView(BasesPostsView):
    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('query')
        if query:
            qs = qs.filter(title__icontains=query)
        return qs

    def get_context_data(self, **kwargs):
        query = self.request.GET.get('query')
        return super().get_context_data(query=query)



class CategoryView(BasesPostsView):
    def get_queryset(self):
        qs = super().get_queryset()
        cate_id = self.kwargs.get('category_id')
        qs = qs.filter(category_id=cate_id)
        return qs


class TagView(BasesPostsView):
    def get_queryset(self):
        tag_id = self.kwargs.get('tag_id')
        try:
            tag = Tag.objects.get(id=tag_id)
        except Tag.DoesNotExist:
            return []
        posts = tag.posts.all()
        return posts


class AuthorView(BasesPostsView):
    def get_queryset(self):
        author_id = self.kwargs.get('author_id')
        if author_id:
            qs = super().get_queryset().filter(owner_id=author_id)
        return qs


class PostView(CommonMixin, CommentMixIn, DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        # import pdb; pdb.set_trace()
        self.pv_uv()
        return response

    def pv_uv(self):
        sessionid = self.request.COOKIES.get('sessionid')
        if not sessionid:
            return
        path = self.request.path
        pv_key = 'pv:{0}{1}'.format(sessionid, path)
        uv_key = 'uv:{0}{1}'.format(sessionid, path)
        if not cache.get(pv_key):
            self.object.increase_pv()
            cache.set(pv_key, 1, 30)
    
        if not cache.get(uv_key):
            self.object.increase_uv()
            cache.set(uv_key, 1, 60 * 60 *24)
    