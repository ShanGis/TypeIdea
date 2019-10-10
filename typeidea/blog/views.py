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

    
'''
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
    
    '''
 

    

    

# def post_detail(request, pk=None):
#     try:
#         queryset = Post.objects.get(pk=pk)
#     except Post.DoesNotExist:
#         raise Http404('好像没有你要找的文章呐')

#     context = {
#         'post': queryset
#     }
#     return render(request, 'blog/detail.html', context=context)
