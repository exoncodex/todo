from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.models import User


# Create your views here.
def home(request):
  return render(request,"todo.html")
def loginpage(request):
  return render(request,"login.html")
def register(request):
  if request.method == "POST":
    username=request.POST.get("username")
    password=request.POST.get("password")
    email=request.POST.get("email")
    if User.objects.filter(username=username,email=email):
      messages.error(request,"User already Exist")
    else:
      ussave=User.objects.create_user(
        username=username,
        email=email,
        password=password
        ) 
      ussave.save()
  return render(request,"register.html")
def logoutpage(request):
  logout(request)
  return redirect("home")
  