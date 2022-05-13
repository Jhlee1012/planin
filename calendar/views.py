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


def test_load_events(request) :
    jinhyun_events = Event.objects.filter(owner_id=16) #쿼리셋
    event_list = list(jinhyun_events.values('title','start_date','end_date'))
    print(event_list) # [{'title': '치맥', 'start_date': datetime.datetime(2022, 5, 8, 16, 0, tzinfo=<UTC>), 'end_date': datetime.datetime(2022, 5, 8, 18, 0, tzinfo=<UTC>)}, {'title': '치맥', 'start_date': datetime.datetime(2022, 5, 14, 2, 0, tzinfo=<UTC>), 'end_date': datetime.datetime(2022, 5, 14, 4, 0, tzinfo=<UTC>)}]
    return JsonResponse({
        "events" : event_list
    })
    # return HttpResponse(render(request,'calendar.html',test_jinhyun))