from django.shortcuts import render,HttpResponse
from .models import User
from django.db import connection
# Create your views here.
def login(request):
    try:
        name=request.GET.get("name","Defalut name")
        pwd=request.GET.get("pwd","0")
        user=User.objects.get(username__exact=name)
        print(user.password)
    except:
        return HttpResponse("Not Found")
    else:
        if user.password==pwd:
            return HttpResponse(user.username)
        else:
            return HttpResponse("Not Found")
