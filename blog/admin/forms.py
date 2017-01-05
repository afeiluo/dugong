from django import forms
# from django.utils.translation import ugettext_lazy as _
from blog.models import Post

class BlogAdminForm(forms.ModelForm):

    tags        = forms.CharField(
                    widget=forms.TextInput(attrs={'class':'form-control'}),
                    required=False,
                )


    def __init__(self, *args, **kwargs):
        super(BlogAdminForm, self).__init__(*args, **kwargs)
        self.fields['tags'].initial = ','.join([ row.name for row in self.instance.tags.all()])

    def save(self, commit=True):
        _tags               = self.cleaned_data.get('tags')
        self.instance.tags  = _tags
        return super(BlogAdminForm, self).save(commit)

    class Meta:
        model   = Post
        fields  = forms.ALL_FIELDS
        # labels  = {
        #     'creator': _('author'),
        # }
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'status': forms.Select(attrs={'class':'form-control'}),
        }



