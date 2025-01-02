
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
    
     

    path('contactez-nous/', views.contactez_nous, name='contactez_nous'),
    path('login_etd/', views.login_etd, name='login_etd'),
    path('contact', views.contact, name='contact'), # had smiya name hiya li kandiro fredirect 
    #path('espace-etudiant/', views.espace_etudiant, name='espace_etudiant'),  # Page après connexion
    
    path('message-bien-envoye/', views.message_bien_envoyer, name='message_bien_envoye')


]
