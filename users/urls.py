from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('login_form/', views.login_form, name='login_form'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login' )
]