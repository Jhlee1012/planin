from django.urls import path
from . import views 

app_name = "model_test"

urlpatterns = [
    #주소, views.landing 함수 실행
    path('', views.enter, name="model_test"),
    path('stop/', views.exit, name="model_test_stop"),
]
