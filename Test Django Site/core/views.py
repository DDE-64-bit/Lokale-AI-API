from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import redirect
from django.contrib .auth.models import User, auth
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .models import *

@login_required(login_url="login")
def index(request):
    return render(request, "index.html")

def login(request):
    return render(request, "login.html")

def aanmelden(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Gegevens zijn verkeerd')
                return redirect('aanmelden')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Gegevens zijn verkeerd')
                return redirect('login')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                #log user in and redirect to settings page
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)


                return redirect('login')
        else:
            messages.info(request, 'Wachtwoorden verschillen')
            return redirect('aanmelden')
        
    else:
        return render(request, 'aanmelden.html')
    
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None: # kijkt of de user bestaat
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "Gegevens Ongeldig")
            return redirect("/login")
        
    else:
        return render(request, "login.html")
    
    
@login_required(login_url="login")
def uitloggen(request):
    auth.logout(request)
    return redirect("login")
