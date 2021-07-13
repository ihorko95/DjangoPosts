from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

from .models import *

class ObjectDetailMixin:
    model = None
    template = None
    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower(): obj})

class ObjectCreateMixin:
    form_model = None
    tamplate = None
    def get(self, request):
        form = self.form_model
        return render(request, self.tamplate, context={'form': form})

    def post(self,request):
        bound_form = self.form_model(request.POST)
        if bound_form.is_valid():
            new_tag = bound_form.save()
            return  redirect(new_tag)
        return render(request, self.tamplate, context={'form': bound_form})