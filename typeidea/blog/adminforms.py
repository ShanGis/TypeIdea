from ckeditor_uploader.widgets import CKEditorUploadingWidget
from xadmin.layout import Fieldset,Row
from dal import autocomplete
from django import forms

from  .models import Post, Category, Tag


class PostAdminForm(forms.ModelForm):
    dec = forms.CharField(widget=forms.Textarea, label='描述', required=False)
    content = forms.CharField(widget=CKEditorUploadingWidget(), label="内容")
    # category = forms.ModelChoiceField(
    #     queryset = Category.objects.all(),
    #     widget=autocomplete.ModelSelect2(url='category-autocomplete'),
    #     label='分类',
    # )
    # tag = forms.ModelMultipleChoiceField(
    #     queryset = Tag.objects.all(),
    #     widget=autocomplete.ModelSelect2Multiple(url='tag-autocomplete'),
    #     label='标签',
    # )

    # class Meta():
    #     model = Post
    #     fields = (
    #         'category', 
    #         'tag',
    #         'dec',
    #         'content',  
    #         'status',
    #     )
