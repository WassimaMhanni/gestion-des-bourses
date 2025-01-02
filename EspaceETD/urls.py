
from django.urls import path
from .views import * 
from . import views
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
#est un ensemble de lien
urlpatterns = [
    #path('',home,name="Aceuill"),
    #path('login',login,name="login"),
    #path('register',register,name="register"),
     


    #path('login_etd/', views.login_etd, name='login_etd'),
    path('espace_etudiant/', views.espace_etudiant_view, name='espace_etudiant'),  # Page après connexion
    path('espace_etudiant/formulaire.html', views.formulaire_candidature, name='formulaire'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
   
   path('espace_etudiant/confirmation_page.html', views.confirmation_formulaire, name='confirmation_formulaire')
    

]
