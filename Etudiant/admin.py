from django.contrib import admin

# Register your models here.
#la  relatio  avec  la  console  de  l'admin
from django.contrib import admin
from .models import Etudiant, PersonnelAdministratif

@admin.register(Etudiant)
class EtudiantAdmin(admin.ModelAdmin):
    list_display = ('email', 'Password', )  # Colonnes affichées
    search_fields = ('email', 'Password', )  # Champs pour recherche

@admin.register(PersonnelAdministratif)
class PersonnelAdministratifAdmin(admin.ModelAdmin):
    list_display =  ('email', 'Password', )
    search_fields =  ('email', 'Password', )
    
    from django.contrib import admin
from .models import Message

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')  # Affiche le nom et l'email dans la liste
    search_fields = ('name', 'email', 'message')  # Ajoute une barre de recherche
    list_filter = ('email',)  # Permet de filtrer par email

