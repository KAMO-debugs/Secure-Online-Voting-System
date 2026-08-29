from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('logout/', views.user_logout, name='logout'),
    path('admin-dashboard/elections/', views.manage_elections, name='manage_elections'),
    path('admin-dashboard/elections/create/',views.create_election,name='create_election'),
    path('', views.home, name='home'),
]