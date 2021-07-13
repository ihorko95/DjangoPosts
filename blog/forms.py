from django import forms
from django.core.exceptions import ValidationError
from .models import Post, Tag

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug','tags','body']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-select','aria-label':"multiple select example"}),
            'body': forms.Textarea(attrs={'class': 'form-control'})
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower().strip()
        if new_slug in ['create', 'delete', 'rename', 'remove']:
            raise ValidationError('Slug can not be "{}"'.format(str(new_slug)))
        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('Slug must be unique. We have already "{}" slug'.format(str(new_slug)) )
        return new_slug


class TagForm(forms.ModelForm):
    # title = forms.CharField(max_length=50)
    # slug = forms.CharField(max_length=50)
    #
    # title.widget.attrs.update({'class': 'form-control'})
    # slug.widget.attrs.update({'class': 'form-control'})
    class Meta:
        model = Tag
        fields = ['title','slug']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'})
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower().strip()
        if new_slug in ['create', 'delete', 'rename', 'remove']:
            raise ValidationError('Slug can not be "{}"'.format(str(new_slug)))
        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('Slug must be unique. We have already "{}" slug'.format(str(new_slug)) )
        return new_slug
