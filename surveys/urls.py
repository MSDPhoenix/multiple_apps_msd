from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='main_page2'),
    path('new',views.new,name='new')
]