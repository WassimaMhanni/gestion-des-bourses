
from django.urls import path
from .views import * 
from . import views
from django.urls import path
from . import views
#est un ensemble de lien
urlpatterns = [
    path('',home,name="Aceuill"),
    path('login',login,name="login"),
    path('register',register,name="register"),
     


    path('login_etd/', views.login_etd, name='login_etd'),
    #path('espace-etudiant/', views.espace_etudiant, name='espace_etudiant'),  # Page après connexion

]
