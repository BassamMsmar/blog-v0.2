from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Post

class PostList(ListView):
    model = Post


class PostDetail(DetailView):
    model = Post

class PostEdit(UpdateView):
    model = Post
    fields =  ('content',)
    template_name = 'post/post_edit.html'
    success_url = '/cbv/'

class Postcreate(CreateView):
    model = Post
    fields =  ('title','content',)
    template_name = 'post/post_edit.html'
    success_url = '/cbv/'

class PostDelete(DeleteView):
    model = Post
    success_url = '/cbv/'
    