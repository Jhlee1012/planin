from django.urls import path
from . import views 

app_name = "viewer_cal"

urlpatterns = [
    path('',views.calendar),
    path('<int:viewer_id>/',views.viewer_cal,name="viewer_cal"),
]
