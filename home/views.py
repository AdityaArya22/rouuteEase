from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')
def signuppage(request):
    return render(request,'signup.html')
def loginpage(request):
    return render(request,'login.html')
def main(request):
    return render(request,'main.html')