from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    print("rubber baby buggy bumpers")
    return render(request, "users/index.html")