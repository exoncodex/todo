from django.shortcuts import render,redirect
from django.contrib.auth import logout


# Create your views here.
def home(request):
  return render(request,"todo.html")
def loginpage(request):
  return render(request,"login.html")
def register(request):
  return render(request,"register.html")
def logoutpage(request):
  logout(request)
  return redirect("home")
  