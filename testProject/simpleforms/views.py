from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as signin

def register(request):
    if request.method=='GET':
        return render(request, 'simpleforms/register.html')
    else:
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']

        new_user=User.objects.create_user(username=email, first_name=first_name,
                                          last_name=last_name, email=email, password=password)
        user=authenticate(username=email, password=password)
        if user is not None:
            signin(request, user)
            return redirect('/motivational/home/')
        else:
            return render(request, 'simpleforms/register.html')

def login(request):
    if request.method=='GET':
        return render(request, 'simpleforms/login.html')
    else:
        email=request.POST['email']
        password=request.POST['password']
    user=authenticate(username=email, password=password)
    if user is not None:
        signin(request, user)
        return redirect('/motivational/home/')
    else:
        return render(request, 'simpleforms/login.html')


def home(request):
    if request.user.is_authenticated:
        return HttpResponse("worked")
    else:
        return HttpResponse("nah")
