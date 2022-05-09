from django.urls import path
from . import views 

app_name = "viewer_cal"

urlpatterns = [
    path('',views.calendar),
]
