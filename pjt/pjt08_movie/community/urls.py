from django.urls import path
from . import views

app_name = 'community'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:review_pk>/', views.detail, name='detail'),
    path(
        '<int:review_pk>/comments/create/',
        views.create_comment,
        name='create_comment',
    ),
    path('<int:review_pk>/like/', views.like, name='like'),
    path('<int:review_pk>/re_comment/<int:comment_pk>/', views.re_comment, name='re_comment'),
    path('<int:review_pk>/like/<int:comment_pk>/', views.like_comment, name='like_comment'),
]
