from django.urls import path
from .views import (
    register_view, login_view, logout_view, create_superuser_view, dashboard_view
)

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', dashboard_view, name='dashboard'),
    path('create-superuser/', create_superuser_view, name='create_superuser'),
]
