from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
#from django.http import HttpResponse
from .models import Post, Tag
from django.views.generic import View
from django.urls import  reverse
from .forms import TagForm, PostForm
from django.contrib.auth.mixins import LoginRequiredMixin

from .utils import *

def hello(request):
    p= Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': p})

class PostCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    form_model = PostForm
    template = 'blog/post_create.html'
    raise_exception = True
class PostUpdate(LoginRequiredMixin, ObjectUpdateMixin,View):
    model = Post
    form_model = PostForm
    template = 'blog/post_update.html'
    raise_exception = True
class PostDelete(LoginRequiredMixin, ObjectDeleteMixin,View):
    model = Post
    template = 'blog/post_delete.html'
    redir = 'post_list_url'
    raise_exception = True

class PostDetail(ObjectDetailMixin,View):
    model = Post
    template = 'blog/post_detail.html'

def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context ={'tags':tags})

class TagDetail(ObjectDetailMixin,View):
    model = Tag
    template = 'blog/tag_detail.html'

class TagCreate(LoginRequiredMixin, ObjectCreateMixin,View):
    form_model = TagForm
    template = 'blog/tag_create.html'
    raise_exception = True
class TagUpdate(LoginRequiredMixin, ObjectUpdateMixin,View):
    model = Tag
    form_model = TagForm
    template = 'blog/tag_update.html'
    raise_exception = True

class TagDelete(LoginRequiredMixin, ObjectDeleteMixin,View):
    model = Tag
    template = 'blog/tag_delete.html'
    redir = 'tags_list_url'
    raise_exception = True



