from django.shortcuts import render
from django.views.generic import ListView

from .models import Post


# Create your views here.
def list_posts(request):
    return render(request, 'post/post_list.html')


class PostList(ListView):
    model = Post
