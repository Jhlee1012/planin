from django.shortcuts import render
from .codes import main

# Create your views here.
def enter(request) :
    main.Main.start()
    return render(request,'index/index.html')

def exit(request) :
    main.Main.stop()
    return render(request,'index/index.html')
