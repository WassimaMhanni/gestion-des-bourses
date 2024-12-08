
from django.urls import path
from .views import * 
from . import views
#est un ensemble de lien
urlpatterns = [
    path('',home,name="Aceuill"),
     path('login',login,name="login"),
       path('register',register,name="register"),
]
