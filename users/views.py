from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def register_form(request):
    return render(request, 'users/register.html')


def register(request):
    username = request.POST.get("username")
    email = request.POST.get("email")
    password = request.POST.get("password")

    if request.method == "POST":
        User.objects.create_user(username=username, email=email, password=password)

    return redirect('/')