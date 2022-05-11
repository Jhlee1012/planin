from django.shortcuts import get_object_or_404
from calendar.models import *


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
    for shared_id in shared_user_ids:
        new_event.shared_users.add(get_object_or_404(User, id=shared_id))
    new_event.save()
    return new_event
