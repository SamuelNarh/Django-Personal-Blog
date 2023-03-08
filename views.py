# from django.http import HttpResponse
from django.shortcuts import render
import datetime
from .models import Blog



# Create your views here.
def index(request):
    blog=Blog.objects.all()
    content={'blog':blog}  
    now= datetime.datetime.now()
    # print(now.day,now.month,now.year,now.hour,now.month,now.microsecond)
    if request.method =="POST":
        message= request.POST['message']
        blog=Blog(date=now,message=message)
        blog.save()   
    return render(request,'index.html',content)

# def edit(request,id):
#     blog=Blog.objects.get(id=id)
#     content={'blog':blog}
#     return render(request,'edit.html',content)