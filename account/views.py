# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth

# Create your views here.

def index(request):
  return render(request,"index.html")



def register(request):
      if request.method=="POST":
          first_name=request.POST['first_name']
          last_name=request.POST['last_name']
          email=request.POST['email']
          username=request.POST['username']
          password1=request.POST['password1']
          password2=request.POST['password2']

          if password1==password2:
             if User.objects.filter(username=username).exists():
                 messages.info(request,"username already taken")
                 return redirect('register.html')
             elif User.objects.filter(email=email).exists():
                  messages.info(request,"email already exists")
                  return redirect('register.html')

             else:
                 user=User.objects.create(username=username,password=password1,email=email,last_name=last_name,first_name=first_name)
                 user.save();
                 messages.info(request,"You have successfully signed up with us")
                 return redirect(request,'login.html')


          else:
             messages.info(request,'passwords not matching')
             return redirect('register.html')


      else:
           return render(request,'register.html')




def login(request):
     if request.method=="POST":
         username=request.POST['username']
         password=request.POST['password']

         user=auth.authenticate(username=username,password=password)

         if user is not None:

            auth.login(request,user)
            return render(request,"customer.html")

         else:
             messages.info(request,"Invalid Credentials")
             return render(request,"login.html")

     else:
         return render(request,"login.html")




def customer(request):
     return render(request,"customer.html")




def logout(request):
    auth.logout(request)
    return redirect(request,"login.html")
