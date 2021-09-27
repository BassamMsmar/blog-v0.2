from django.urls import path

from post import views


urlpatterns = [
    path('', views.list_posts, name = 'list',),
    path('cbv', views.PostList.as_view(), name = 'post_list',),
]