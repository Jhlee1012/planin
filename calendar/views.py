from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from calendar.models import *

# from calendar.create_models import * -> 다른 모델에서 함수 가져오기 나중에 정리용 

# Create your views here.

def calendar(request):
    return render(request,'calendar/calendar.html')


def test_fetch(request):
    import json
    response_body = json.loads(request.body)
    events = response_body.get("events")
    for event in events:
        print(event.keys())
        print(event.get("start"))
        print(event.get("end"))
    return JsonResponse({})



def model_test(request):
    new_event = create_event("my_evet","2022-05-08 16:00:00","2022-05-08 18:00:00", 1)
    return HttpResponse(new_event)

#CRUD - C

def create_user(name,gmail,events) :
    new_user = User()
    new_user.name = name
    new_user.gmail = gmail
    new_user.events = events
    new_user.save()
    #중복처리?
    return new_user 


def create_event(title,start_date,end_date,owner_id, shared_user_ids=[]) :
    new_event = Event()
    new_event.title = title
    new_event.start_date = start_date
    new_event.end_date = end_date
    new_event.owner = get_object_or_404(User, id=owner_id)
    return new_event
#     for shared_id in shared_user_ids:
#         new_event.shared_users.add(get_object_or_404(User, id=shared_id))
#     new_event.save()
#     


def add_shared_user_to_event(event_id, user_id):
    target_event = get_object_or_404(Event, id=event_id)
    target_event.shared_users.add(get_object_or_404(User, id=user_id))
    target_event.save()


def get_user(user_id):
    a_user=User.objects.get(id = user_id)
    # user_events = Event.objects.get(id = user_id)
    print(f"this user is : {a_user.name}") 
    # print(f"User's events : {user_events.events}")   

def get_evnet(event_id):
    a_event=Event.objects.get(id = event_id)
    all_events = Event.objects.all()
    print(f"this event is : {a_event.title},") 
    # print(f"User's events : {user_events.events}")   


def delete_user(user_id):
    a_user=User.objects.get(id = user_id)
    a_user.delete()
    return 

#유저 다 지우기
#     users = User.objects.all()
#     for user in users :
#         delete_user(user.id)

#     return HttpResponse(users)

## create test