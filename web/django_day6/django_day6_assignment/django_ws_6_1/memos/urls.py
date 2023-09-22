from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:memo_pk>/', views.detail, name='detail'),
    path('<int:memo_pk>/delete', views.delete, name='delete'),
]
