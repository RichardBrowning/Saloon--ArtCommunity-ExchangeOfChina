from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'accounts/dashboard.html')
    #return HttpResponse('home')
def gallery(request):
    return HttpResponse('gallery')

def register(request):
    context = {}
    return render(request, 'accounts/register.html', context)

def login(request):
    context = {}
    return render(request, 'accounts/login.html', context)