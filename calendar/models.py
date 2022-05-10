from django.db import models
# from django.contrib.auth.models import User

# Create your models here.

class User(models.Model) :
    name = models.CharField(max_length=32)
    gmail = models.EmailField(max_length=254)
    events = models.CharField(max_length=32)


class Event(models.Model) :
    title = models.ForeignKey(User,on_delete=models.CASCADE,related_name = "user_event")
    start_date = models.DateTimeField() #%Y-%m-%d %H:%M:%S
    end_date = models.DateTimeField() #%Y-%m-%d %H:%M:%S
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="event_owner")
    shared_users = models.ManyToManyField(User, related_name="shared_events")




