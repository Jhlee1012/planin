from django.contrib import admin
from django.urls import path
from . import views

app_name = "settings"

urlpatterns = [
    path('login/',views.login,name ="login"),
    path('dashboard/',views.dashboard,name = "dashboard"),
    path('setup/',views.setup, name = "setup"),
]