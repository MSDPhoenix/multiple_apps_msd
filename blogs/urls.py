from django.urls import path
from .import views

# app_name = 'blogs'
urlpatterns = [
    path('',views.index,name='main_page'),
    path('new',views.new,name='new'),
    path('create',views.create),
    path('<int:id>',views.show),
    path('<int:id>/edit',views.edit),
    path('<int:id>/delete',views.destroy),
]
