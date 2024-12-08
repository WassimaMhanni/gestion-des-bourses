from django.db import models

# Create your models here.
#les  modèle  on ici  la  structure  de  l'etudiant  qui  sont les  champs qui créer  dans la  base de  données*
from django.db import models

class Etudiant(models.Model):
    email = models.EmailField(unique=True)
    Password = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.email} ({self.Password})"

class PersonnelAdministratif(models.Model):
    email = models.EmailField(unique=True)
    Password = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.email} ({self.Password})"

