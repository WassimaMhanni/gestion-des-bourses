from django import forms
from .models import DossierDeCandidature

class DossierDeCandidatureForm(forms.ModelForm):
    class Meta:
        model = DossierDeCandidature
        fields = [
            'nom', 'prenom', 'cin', 'email', 'tel', 'lieu_naissance', 'adresse',
            'emploi_tuteur', 'revenu_tuteur', 'personnes_charge', 'cin_file', 'revenu_file',
            'attestation_habitation_file', 'bac_upload', 'ville_habitation', 'ville_etude', 'niveau'
        ]
        
        
