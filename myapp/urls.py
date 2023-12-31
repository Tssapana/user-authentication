from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_request, name='register'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('restricted/', views.restricted_page, name='restricted'),
    path('', views.home, name='home'),
]