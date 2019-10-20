from ckeditor_uploader.widgets import CKEditorUploadingWidget
from dal import autocomplete
from django import forms

from  .models import Category,Tag


class PostAdminForm(forms.ModelForm):
    # status = forms.BooleanField(label='是否删除', required=False)
    dec = forms.CharField(widget=forms.Textarea, label='描述', required=False)
    content = forms.CharField(widget=CKEditorUploadingWidget(), label="内容")
    import pdb; pdb.set_trace()
    category = forms.ModelChoiceField(
        queryset = Category.objects.all(),
        widget=autocomplete.ModelSelect2(url='category-autocomplete'),
        label='分类',
    )
    tag = forms.ModelMultipleChoiceField(
        queryset = Tag.objects.all(),
        widget=autocomplete.ModelSelect2Multiple(url='tag-autocomplete'),
        label='标签',
    )