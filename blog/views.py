from django.shortcuts import render
#from django.http import HttpResponse
from .models import Post

def hello(request):
    p= Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': p})

def post_detail(request, slug):
    p = Post.objects.get(slug__iexact=slug)
    return render(request, 'blog/post_detail.html',context={'post': p})