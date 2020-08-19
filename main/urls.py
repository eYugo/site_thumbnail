from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('vote/<str:pk>/confirm', views.VoteConfirm, name='vote-confirm'),
    path('post/new/', views.PostCreate, name='post-create'),
    path('thumb/delete/<str:pk>/', views.ThumbDelete, name='thumb-delete'),
    path('myposts/', views.MyPostsView, name='my-posts'),
    path('post/<str:pk>/delete/', views.PostDeleteView, name='post-delete'),
    path('post/<str:pk>/', views.PostDetailView, name='post'),
    path('post/<str:pk>/result', views.PostResultView, name='post-result'),

]
