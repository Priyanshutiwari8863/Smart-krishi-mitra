from django.urls import path
from . import views

urlpatterns = [

    # Login page
    path('login/', views.login_view, name='login'),

    # Register page
    path('register/', views.register, name='register'),
   
    # Dashboard page
    path('dashboard/', views.dashboard, name='dashboard'),

    # Profile page
    path('profile/', views.profile, name='profile'),

    # Admin Dashboard
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),

    # Logout
    path('logout/', views.logout_view, name='logout'),

    # Edit profile
    path('edit-profile/', views.edit_profile, name='edit_profile'),

]