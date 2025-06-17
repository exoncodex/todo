from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.models import User
from django.contrib import messages
from todoapp.models import Todo
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    if request.user.is_anonymous:
        return redirect("login")
    if request.method == "POST":
        task=request.POST.get("task")
        usave=Todo(user=request.user,todoname=task)
        usave.save()
    all_todo=Todo.objects.filter(user=request.user)
    context={
       "todos":all_todo
     }
    return render(request, "todo.html",context)
def loginpage(request):
  if request.method == "POST":
    passw=request.POST.get("passw")
    uname=request.POST.get("uname")
    authe=authenticate(password=passw,username=uname)
    if authe is not None:
      login(request,authe)
      return redirect("home")
    else:
      messages.error(request,"wrong username or password")
  return render(request,"login.html")
def register(request):
  if request.method == "POST":
    username=request.POST.get("username")
    password=request.POST.get("password")
    email=request.POST.get("email")
    if User.objects.filter(username=username).exists():
      messages.error(request,"User already Exist")
    elif User.objects.filter(email=email).exists():
      messages.error(request, "Email already in use")
    else:
      ussave=User.objects.create_user(
        username=username,
        email=email,
        password=password
        ) 
      ussave.save()
      messages.success(request,"User has been created")
      return redirect("login")
  return render(request,"register.html")
def logoutpage(request):
  logout(request)
  return redirect("login")
@login_required
def delete(request,name):
    task=get_object_or_404(Todo,user=request.user,todoname=name)
    task.delete()
    return redirect('home')
@login_required
def update(request,name):
  task=get_object_or_404(Todo,user=request.user,todoname=name)
  task.status = True
  task.save()
  return redirect("home")
 
  