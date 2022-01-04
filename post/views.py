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
    fields =  ('title','content',)
    template_name = 'post/post_edit.html'
    success_url = '/'

class PostCreate(CreateView):
    model = Post
    fields =  ('title','content',)
    template_name = 'post/post_create.html'
    success_url = '/'

class Postcreate(DeleteView):
    model = Post
    success_url = '/'