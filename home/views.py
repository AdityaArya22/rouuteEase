from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import User
 
# Create your views here.
def home(request):
    return render(request,'index.html')
def signuppage(request):
    if request.method == "POST":
        username = request.POST.get('username').strip()
        password = request.POST.get('password').strip()
        email = request.POST.get('email').strip()

        if not username or not password or not email:
            messages.error(request, "Please fill in all fields")
            return redirect('/')

        user = User.objects.filter(username=username)
        if user.exists():
            messages.error(request, "Username alreday exists")
            return redirect('/')

        user = User.objects.create(
            username=username,
            email=email
        )
        user.set_password(password)
        user.save()

        return redirect('/loginpage/')
    return render(request, "signup.html")


def loginpage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        username = username.strip()

        if not username:
            messages.error(request, "Please enter your email")
            return redirect('/loginpage/')

        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request, "Invalid username or password")
            return redirect('/loginpage/')
        else:
            login(request, user)
            return redirect('/home/')

    return render(request, "login.html") 
def main(request):
    return render(request,'main.html')