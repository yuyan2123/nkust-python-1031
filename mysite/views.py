from django.shortcuts import render
from django.http import HttpResponse
from mysite.models import PlayList, Video
import random

def index(request):
    lucky_no = random.randint(1,42)
    numbers = list()

    for i in range(6):
        numbers.append(random.randint(1,42))
    
    return render(request,"index.html",locals())

def playlist(request):
    items = PlayList.objects.all()
    return render(request, "playlist.html", locals())

def showlist(request,id):
    titles = Video.objects.filter(plist=id)
    return render(request, "showlist.html", locals())
