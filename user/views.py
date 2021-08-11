from django.core.checks import messages
from user.models import UserInfo
from django.http import HttpResponse
from .forms import UserInfoForm
from django.shortcuts import render, redirect 
from django.template import Context
from django.views.generic import ListView
from django.contrib import messages

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def User(request):
    depts = UserInfo.objects.all()
    return render(request, "dashboard.html",{'depts':depts})

def Usershow(request):
    context ={} 
    form =  UserInfoForm(request.POST or None, request.FILES or None) 
    if form.is_valid(): 
        form.save() 
    context['form']= form 
    return render(request, 'create_user.html',context)

def addUser(request):
    if (request.method=="GET"):
        form  = UserInfoForm()
        return render(request,'create_user.html',{"form":form})
    else:
        #save code
        form = UserInfoForm(request.POST)
        if form.is_valid():  
            try:  
                form.save()                                    
            except:  
                pass  
        return redirect(User)


def edit(request,id):  
    if(request.method == "GET") :
        d = UserInfo.objects.get(id=id)                
        return render(request,'edit.html',{'emp':d})
    
    elif(request.method == "POST"):
        id = request.POST.get("id")
        d = UserInfo.objects.get(id=id) 
        form = UserInfoForm(request.POST, instance = d)  
        if form.is_valid():  
            form.save()  
        return redirect(User)

def delete(request,id):
    d = UserInfo.objects.filter(id=id)
    d.delete()    
    return redirect(User)
