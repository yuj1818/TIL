from django.urls import path
from . import views

app_name = 'stores'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('create/<int:pk>', views.create_product, name='create_product'),
    path('<int:store_pk>/delete/<int:prod_pk>', views.delete_product, name='delete_product'),
]
