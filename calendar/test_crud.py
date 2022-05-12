from django.shortcuts import get_object_or_404
from calendar.models import *



def test_create_users_and_evnets(request):
   
    user_1 = create_user("이진현",'rig8696@likelion.org')
    print(user_1.id, user_1.name)
    user_2 = create_user("오한나",'jane6966@likelion.org')
    print(user_2.id, user_2.name)
    user_3 = create_user("지승민",'dove_creative@likelion.org')
    print(user_3.id, user_3.name)
    
    user_1_event = create_event("치맥","2022-05-08 16:00:00","2022-05-08 18:00:00", user_1.id)
    print(user_1_event.id, user_1_event.title)
    user_2_event = create_event("미팅","2022-05-08 15:00:00","2022-05-08 17:00:00", user_2.id)
    print(user_2_event.id, user_2_event.title)
    user_3_event = create_event("저녁","2022-05-09 13:00:00","2022-05-08 14:00:00", user_3.id)
    print(user_3_event.id, user_3_event.title)

    add_shared_user_to_event(user_1_event.id,user_2.id)
    add_shared_user_to_event(user_2_event.id,user_3.id)
    add_shared_user_to_event(user_3_event.id,user_1.id)


    return JsonResponse({
        "status": "success"
    })


#유저 다 지우기
def test_delete_users(request):
    users = User.objects.all()
    for user in users :
        delete_user(user.id)

    return HttpResponse(users)


def get_user(user_id):
    a_user=User.objects.get(id = user_id)
    # user_events = Event.objects.get(id = user_id)
    print(f"this user is : {a_user.name}") 
    # print(f"User's events : {user_events.events}")   

def get_event(event_id):
    a_event=Event.objects.get(id = event_id)
    all_events = Event.objects.all()
    print(f"this event is : {a_event.title},") 
    # print(f"User's events : {user_events.events}")   


def test_fetch(request):
    import json
    response_body = json.loads(request.body)
    events = response_body.get("events")
    for event in events:
        print(event.keys())
        print(event.get("start"))
        print(event.get("end"))
    return JsonResponse({})

def test_show_user_name(request,user_id) : 
    #user가 user id 캘린더로 들어왔을 때, 
    #DB에서 id 로  user name 가져오기
    a_user = User.objects.get(id = user_id)
    context ={
        "id":a_user.id,
        "name" : a_user.name, 
        "email" : a_user.gmail,
        }
    #htm에서 "user name 의 캘린더 입니다"로 출력하기 
    return render(request,'calendar/calendar.html',context) 
