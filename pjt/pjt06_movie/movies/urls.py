from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:movie_pk>/detail/', views.detail, name='detail'),
    path('<int:movie_pk>/update/', views.update, name='update'),
    path('<int:movie_pk>/delete/', views.delete, name='delete'),
    path('<int:movie_pk>/comments/', views.comments_create, name='comments_create'),
    path('<int:movie_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
    path('<int:movie_pk>/likes/', views.likes, name='likes'),
    path('<int:user_pk>/like_movies/', views.like_movie_list, name='like_movie_list'),
    path('<int:movie_pk>/comments/<int:comment_pk>/', views.re_comment, name="re_comment"),
    path('<int:movie_pk>/re_comment/<int:comment_pk>/delete/', views.re_comment_delete, name='re_comment_delete')
]
