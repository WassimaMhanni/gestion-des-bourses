from django.db import models

# Create your models here.
from django.db import models

from django.db import models

class DossierDeCandidature(models.Model):
    # Informations personnelles
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    cin = models.CharField(max_length=20)
    email = models.EmailField()
    tel = models.CharField(max_length=15)
    lieu_naissance = models.CharField(max_length=255)
    adresse = models.TextField()
    
    # Informations sur le tuteur
    emploi_tuteur = models.CharField(max_length=255)
    revenu_tuteur = models.DecimalField(max_digits=10, decimal_places=2)
    personnes_charge = models.IntegerField()
    
    # Fichiers téléchargeables (avec possibilité de null)
    cin_file = models.FileField(upload_to='cin_files/', null=True, blank=True)
    revenu_file = models.FileField(upload_to='revenu_files/', null=True, blank=True)
    attestation_habitation_file = models.FileField(upload_to='attestations_habitation/', null=True, blank=True)
    bac_upload = models.FileField(upload_to='uploads/bac/', null=True, blank=True)
    
    # Informations supplémentaires
    ville_habitation = models.CharField(max_length=255)
    ville_etude = models.CharField(max_length=255)
    
    # Informations académiques
    niveau = models.CharField(max_length=20, choices=[
    ('licence', 'Licence'),
    ('master', 'Master'),
    ('doctorat', 'Doctorat')
], default='licence')  # Valeur par défaut ajoutée ici

    # Date de création et mise à jour
    date_creation = models.DateTimeField(auto_now_add=True)
    date_mise_a_jour = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nom} {self.prenom} - {self.email}"
