from tracemalloc import start
from turtle import title
from venv import create
from django.forms import NullBooleanField
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from calendar.models import *
from calendar.create_models import *
from calendar.test_crud import *
import json

# Create your views here.

def calendar(request):
    return render(request,'calendar/calendar.html')


def save_events(request):
    response_body = json.loads(request.body)
    events = response_body.get("events")

    for event in events: 
        title = event.get("title") 
        start_date = event.get("start")
        end_date = event.get("end") 
        
        create_event(title,start_date,end_date)
    
    return JsonResponse({})


def create_event(title,start_date,end_date) :
    new_event = Event()
    new_event.title = title
    new_event.start_date = start_date
    new_event.end_date = end_date
    #new_event.owner = get_object_or_404(User, id= owner_id)
    new_event.save()
    # print(new_event.owner.id, new_event.owner.name)
