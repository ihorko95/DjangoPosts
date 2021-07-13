from django import forms
from django.core.exceptions import ValidationError
from .models import Tag


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
            'title': forms.TimeInput(attrs={'class': 'form-control'}),
            'slug': forms.TimeInput(attrs={'class': 'form-control'})
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower().strip()
        if new_slug in ['create', 'delete', 'rename', 'remove']:
            raise ValidationError('Slug can not be "{}"'.format(str(new_slug)))
        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('Slug must be unique. We have already "{}" slug'.format(str(new_slug)) )
        return new_slug

    # def save(self):
    #     new_tag =Tag.objects.create(
    #         title=self.cleaned_data['title'],
    #         slug=self.cleaned_data['slug']
    #     )
    #     return new_tag
