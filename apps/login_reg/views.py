from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User
from django.core.urlresolvers import reverse


def index(request):
    print("fuck django...")
    return render(request, "login_reg/index.html")


def success(request):
    return render(request, "login_reg/success.html")


def register(request):
    errors = User.objects.reg_validation(request.POST)
    if errors:
        print("*"*80)
        print("ERRORS!!!")
        print("*"*80)
    return redirect(reverse('login_reg:success'))


def login(request):
    print("login route")
    return redirect(reverse('login_reg:success'))


def error(request):
    return render(request, "login_reg/404.html") 