from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('members/', views.show_members, name='show_members'),
    path('update/', views.update, name='update'),
    path('<int:user_pk>/authority/', views.change_authority, name='change_authority'),
    path('<int:user_pk>/delete/', views.member_delete, name='member_delete'),
]
