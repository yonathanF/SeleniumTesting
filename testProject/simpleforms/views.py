from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as signin
from simpleforms.models import Quote
import random

def register(request):
    if request.method=='GET':
        return render(request, 'simpleforms/register.html')
    else:
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        try:
            new_user=User.objects.create_user(username=email, first_name=first_name,
                                          last_name=last_name, email=email, password=password)

            user=authenticate(username=email, password=password)
            if user is not None:
                signin(request, user)
                return redirect('/motivational/home/')
            else:
                return render(request, 'simpleforms/register.html',{"error":"Try again."})
        except:
            return render(request, 'simpleforms/register.html', {"error":"Try again with a different email"})
def login(request):
    if request.method=='GET':
        return render(request, 'simpleforms/login.html')
    else:
        email=request.POST['email']
        password=request.POST['password']
        try:
            user=authenticate(username=email, password=password)
            if user is not None:
                signin(request, user)
                return redirect('/motivational/home/')
            else:
                return render(request, 'simpleforms/login.html', {"error": "Can't find that account. Try again please."})
        except:
            return render(request, 'simpleforms/login.html', {"error": "Can't find that account. Try again please."})


def home(request):
    if request.user.is_authenticated:
        qId=random.randint(1,11)
        quote=Quote.objects.get(pk=qId)
        
        context={"name":request.user.first_name+" "+request.user.last_name,
                 "author":quote.author, "content":quote.content}

        return render(request, 'simpleforms/home.html', context)
    else:
        return redirect('/motivational/login/')
