from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from calendar.models import *

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

## 삭제 테스트 - 왜 안되지..?
# def model_test(request,user_id):
#     users = User.objects.get(id = user_id)
#     for user in users :
#         delete_user(user)
#         user = user+1

#     return HttpResponse(users)

## create test

def model_test(request):
    new_event = create_event("my_evet","2022-05-08 16:00:00","2022-05-08 18:00:00","이진현","김비안,김지석")
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


def create_event(title,start_date,end_date,owner_id,shared_users) :
    new_event = Event()
    new_event.title = title
    new_event.start_date = start_date
    new_event.end_date = end_date
    new_event.owner = get_object_or_404(User,id=owner_id)
    new_event.shared_users = get_object_or_404(shared_users,id=shared_users)
    new_event.save()
    return new_event

def delete_user(user_id):
    a_user=User.objects.get(id = user_id)
    a_user.delete()
    return 