from django.urls import path
from . import views
import blogs.views

urlpatterns = [
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('users/new',views.register,name='new_user'),
    path('users',views.user_list,name='users'),
    path('',blogs.views.index)
]