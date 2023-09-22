from django.urls import path
from . import views

app_name = 'garages'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:garage_pk>/edit/', views.edit, name='edit'),
    path('<int:garage_pk>/delete/', views.delete, name='delete'),
    path('<int:garage_pk>/update/', views.update, name='update'),
]
