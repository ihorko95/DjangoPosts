from django.shortcuts import render
#from django.http import HttpResponse
from .models import Post, Tag
from django.views.generic import View
def hello(request):
    p= Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': p})


class PostDetail(View):
    def get(self, request, slug):
        p = Post.objects.get(slug__iexact=slug)
        return render(request, 'blog/post_detail.html', context={'post': p})
def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context ={'tags':tags})

class TagDetail(View):
    def get(self, request,slug):
        tag = Tag.objects.get(slug__iexact=slug)
        return render(request, 'blog/tag_detail.html', context={'tag': tag})