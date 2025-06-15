#importation 
from django.urls import path
from todoapp import views

#urls
urlpatterns = [
  path("",views.home,name="home"),
  path("login/",views.loginpage,name="login"),
  path("register/",views.register,name="register"),
  path("logout/",views.logoutpage,name="logout")
  ]