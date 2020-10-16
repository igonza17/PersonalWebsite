from django.shortcuts import render
from .models import Courses, PreRequisite
import json
import urllib.request
import time
import os, ssl
#Fixes some issues related to ssl security
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

def website(request):

    return render(request, 'website/website.html')

def final(request):
    data= Courses.objects.all()
    return render(request, 'website/final.html',{"data": data})


def weather(request):
    api_key = "731fdf9aea705b46c11395b36b234a43"
    source = urllib.request.urlopen("https://api.openweathermap.org/data/2.5/weather?zip=30144,&units=imperial&us&appid=" + api_key).read()
    list_of_data = json.loads(source)
    struct_time = time.localtime()
    time_report = time.strftime("%Y-%m-%d, %H:%M:%S", struct_time)
    cur_temp = list_of_data["main"]["temp"]
    return render(request, "website/weather.html", {'city': str(list_of_data['name']), 'temp': str(cur_temp),"pressure": str(list_of_data['main']['pressure']),"speed": str(list_of_data['wind']['speed']),"degree": str(list_of_data['wind']['deg']),"time": str(time_report)})


