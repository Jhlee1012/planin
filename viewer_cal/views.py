from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse

# Create your views here.
def viewer_cal(request,viewer_id) : 
    return render(request,'viewer_cal/calendar.html')

def calendar(request):
    return render(request,'viewer_cal/calendar.html')


def test_fetch(request):
    import json
    response_body = json.loads(request.body)
    events = response_body.get("events")
    for event in events:
        print(event.keys())
        print(event.get("start"))
        print(event.get("end"))
    return JsonResponse({})
