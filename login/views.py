from django.shortcuts import render,HttpResponse
from .models import User
from django.db import connection
# Create your views here.
def index(request):
    users=User.objects.all()
    for user in users:
        print(user.username,user.password,user.date_joined)
    return HttpResponse("<h1>200 OK</h1>")