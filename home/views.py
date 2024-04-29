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
    car_mileages = {
        "Maruti Suzuki Swift": 22,
        "Hyundai Grand i10": 19,
        "Tata Tiago": 23,
        "Maruti Suzuki Baleno": 21,
        "Honda Amaze": 18,
        "Hyundai Venue": 17,
        "Mahindra Bolero": 15,
        "Mahindra Thar": 15,
        "Tata Nexon": 17,
        "Toyota Innova Crysta": 13,
        "Ford EcoSport": 18,
        "Kia Sonet": 18,
        "Renault Kwid": 22,
        "Volkswagen Polo": 18,
        "Maruti Suzuki Alto": 22,
        "Mahindra Scorpio": 15,
        "Tata Altroz": 21,
        "Hyundai Creta": 16,
        "Mahindra XUV300": 17,
        "Honda City": 18,
        # Add more cars here
    }
    return render(request, 'main.html', {'car_mileages': car_mileages})
