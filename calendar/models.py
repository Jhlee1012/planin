from django.db import models
# from django.contrib.auth.models import User

# Create your models here.

#CRUD - C
class User(models.Model) :
    name = models.CharField(max_length=32)
    gmail = models.EmailField(max_length=254)

class Event(models.Model) :
    title = models.CharField(max_length=32)
    start_date = models.DateTimeField() #%Y-%m-%d %H:%M:%S
    end_date = models.DateTimeField() #%Y-%m-%d %H:%M:%S
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="events", null=True, blank=True)
    shared_users = models.ManyToManyField(User, related_name="shared_events") 
