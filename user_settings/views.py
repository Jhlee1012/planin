from django.shortcuts import render

# Create your views here.
def login(request) :
    return render(request,'settings/login.html')

def dashboard(request) :
    return render(request,'settings/dashboard.html')

def setup(request) :
    return render(request,'settings/setup.html')
    