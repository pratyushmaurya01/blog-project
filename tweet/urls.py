from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tweet/', views.tweet_list, name='tweet_list'),
    path('create/', views.tweet_create, name='tweet_create'), 

    path('<int:tweet_id>/edit/', views.tweet_edit, name='tweet_edit'),
    path('<int:tweet_id>/del/', views.tweet_del, name='tweet_del'),
    path('register/',views.register,name='register'),
    path('<int:tweet_id>/detail/', views.tweet_detail, name='detail'),
    path('<int:tweet_id>/like/', views.toggle_like, name='toggle_like')
]