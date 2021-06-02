from django.shortcuts import render


def login_form(request):
    return render(request, 'users/login.html')
