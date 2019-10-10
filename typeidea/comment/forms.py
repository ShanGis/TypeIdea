from django import forms

from .models import Comment


class CommentForms(forms.ModelForm):
    nickname = forms.CharField(
        max_length=50,
        label='网名',
        widget=forms.widgets.Input(
            attrs={'class': 'form-control', 'style': 'width: 60%;' }
        )
    )

    email = forms.EmailField(
        label='邮箱',
        widget=forms.widgets.EmailInput(
            attrs={'class': 'form-control', 'style': 'width: 60%;'}
        )
    )

    websit = forms.URLField(
        label='网址',
        widget=forms.widgets.URLInput(
            attrs={'class': 'form-control', 'style': 'width:60%;'}
        )
    )

    content = forms.CharField(
        max_length=500,
        label='内容',
        widget=forms.widgets.Textarea(
            attrs={
                'rows': 6, 'cols': 60, 'class': 'form-control'}
        )
    )

    



    def clean_content(self):
        clean_data = self.cleaned_data['content']
        if len(clean_data) < 20:
            raise forms.ValidationError('评论长度短于20!')
        return clean_data
        
    class Meta():
        model = Comment
        fields = [
            'nickname', 'email', 'websit', 'content'
        ]