from django.urls import path

from post import views


urlpatterns = [

    path('', views.PostList.as_view(), name='list_post'),
    path('cbv/details/<int:pk>', views.PostDetail.as_view(), name='post_detail'),
    path('cbv/create', views.PostCreate.as_view(), name='post_create'),
    path('cbv/edit/<int:pk>', views.PostEdit.as_view(), name='post_edit'),
    # path('cbv/delete/<int:pk>', views.DeleteView.as_view(), name='post_delete'),

]