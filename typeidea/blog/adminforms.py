from django import forms


class PostAdminForm(forms.ModelForm):
    status = forms.BooleanField(label='是否删除', required=False)
    dec = forms.CharField(widget=forms.Textarea, label='描述', required=False)
    
    def clean_status(self):
        if self.cleaned_data['status']:
            return 1
        else:
            return 2