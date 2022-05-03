from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
def viewer_cal(request,viewer_id) : 
    return render(request,'viewer_cal/calendar.html')

def calendar(request):
    return render(request,'viewer_cal/calendar.html')