from django.urls import path
from .views import signup, profile, edit_profail


app_name= 'accounts'

urlpatterns = [
    path('signup', signup, name='signup' ),
    path('profile', profile, name='profile' ),
    path('profile/edit', edit_profail, name='edit_profail' ),
]