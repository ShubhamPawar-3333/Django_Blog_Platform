# blog_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('post/<int:post_id>/', views.blog_detail, name='blog_detail'),
    path('create/', views.create_post, name='create_post'),
]