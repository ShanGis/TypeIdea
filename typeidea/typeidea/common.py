from blog.models import Post,Category,Tag
from comment.models import Comment
from comment.forms import CommentForms
from config.models import SideBar

class CommonMixin(object):
    def get_category_context(self):
        cates = Category.objects.filter(status=1)
        nav_cates = []
        not_nav_cates = []
        for cate in cates:
            if cate.is_nav:
                nav_cates.append(cate)
            else:
                not_nav_cates.append(cate)
        return {
            'nav_cates': nav_cates,
            'not_nav_cates': not_nav_cates,
        }

    def get_context_data(self, **kwargs):
        # 侧边栏
        side_bars = SideBar.objects.filter(status=1)

        recently_posts = Post.objects.filter(status=1)[:10]
        hot_posts = Post.objects.filter(status=1).order_by('pv')[:10]
        recently_comments = Comment.objects.filter(status=1)[:10]

        # 模板内容
        kwargs.update({
            'side_bars': side_bars,
            'recently_posts': recently_posts,
            'recently_comments': recently_comments,
            'hot_posts':hot_posts
        })
        kwargs.update(self.get_category_context())
        kwargs = super().get_context_data(**kwargs)
        return kwargs 
    

class CommentMixIn(object):
    def get_comments(self):
        target = self.request.path
        comments = Comment.objects.filter(target=target)
        return comments

    def get_context_data(self, **kwargs):
        kwargs.update({
            'comment_form': CommentForms(),
            'comments': self.get_comments()
        })
        return super().get_context_data(**kwargs)