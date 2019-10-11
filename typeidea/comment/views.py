from django.shortcuts import redirect
from django.views.generic import TemplateView

from .models import Comment
from .forms import CommentForms

class CommentView(TemplateView):
    template_name = 'comment/result.html'
    
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = CommentForms(request.POST)
        target = request.POST.get('target')

        if form.is_valid():
            instance = form.save(commit=False)
            instance.target = target
            instance.save()
            succeed = True
            return redirect(target)
        else:
            succeed = False
        
        context = {
            'succeed': succeed,
            'form': form
        }
        return self.render_to_response(context)
