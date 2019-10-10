from django.views.generic import ListView

from .models import Link
from blog.views import CommonMixin
from comment.forms import CommentForms
from typeidea.common import CommonMixin, CommentMixIn


class LinkView(CommonMixin, CommentMixIn, ListView):
    model = Link
    queryset = Link.objects.filter(status=1)
    context_object_name = 'links'
    template_name = 'config/link.html'
