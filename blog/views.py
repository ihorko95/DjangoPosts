from django.shortcuts import render
from django.shortcuts import get_object_or_404
#from django.http import HttpResponse
from .models import Post, Tag
from django.views.generic import View

from .utils import *

def hello(request):
    p= Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': p})


class PostDetail(ObjectDetail,View):
    model = Post
    template = 'blog/post_detail.html'
    # def get(self, request, slug):
    #     # p = Post.objects.get(slug__iexact=slug)
    #     p = get_object_or_404(Post, slug__iexact=slug)
    #     return render(request, 'blog/post_detail.html', context={'post': p})
def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context ={'tags':tags})

class TagDetail(ObjectDetail,View):
    model = Tag
    template = 'blog/tag_detail.html'
    # def get(self, request,slug):
    #     # tag = Tag.objects.get(slug__iexact=slug)
    #     tag = get_object_or_404(Tag,slug__iexact=slug)
    #     return render(request, 'blog/tag_detail.html', context={'tag': tag})