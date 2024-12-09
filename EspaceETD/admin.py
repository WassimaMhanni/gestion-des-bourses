from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import DossierDeCandidature


   
   
   
@admin.register(DossierDeCandidature)
class DossierDeCandidatureAdmin(admin.ModelAdmin):
    list_display = [
        'nom', 'prenom', 'cin', 'email', 'tel', 'lieu_naissance', 'adresse',
        'emploi_tuteur', 'revenu_tuteur', 'personnes_charge', 'cin_file', 'revenu_file',
        'attestation_habitation_file', 'bac_upload', 'ville_habitation', 'ville_etude', 'niveau'
    ]
    search_fields = ['cin', 'email', 'nom', 'prenom']  # Permet de rechercher plus facilement

