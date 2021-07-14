from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
#from django.http import HttpResponse
from .models import Post, Tag
from django.views.generic import View
from .forms import TagForm, PostForm

from .utils import *

def hello(request):
    p= Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': p})

class PostCreate(ObjectCreateMixin, View):
    form_model = PostForm
    template = 'blog/post_create.html'
class PostUpdate(ObjectUpdateMixin,View):
    model = Post
    form_model = PostForm
    template = 'blog/post_update.html'

class PostDetail(ObjectDetailMixin,View):
    model = Post
    template = 'blog/post_detail.html'

def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context ={'tags':tags})

class TagDetail(ObjectDetailMixin,View):
    model = Tag
    template = 'blog/tag_detail.html'

class TagCreate(ObjectCreateMixin,View):
    form_model = TagForm
    template = 'blog/tag_create.html'
class TagUpdate(ObjectUpdateMixin,View):
    model = Tag
    form_model = TagForm
    template = 'blog/tag_update.html'

