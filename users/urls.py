from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login' ),
    path('register_form/', views.register_form, name='register_form'),
    path('register/', views.register, name='register')
]