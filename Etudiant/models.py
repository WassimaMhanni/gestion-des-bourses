from django.db import models

# Create your models here.
#les  modèle  on ici  la  structure  de  l'etudiant  qui  sont les  champs qui créer  dans la  base de  données*
from django.db import models

class Etudiant(models.Model):
    nom = models.CharField(max_length=50, default='Inconnu')  # Valeur par défaut
    prenom = models.CharField(max_length=50, default='Inconnu')  # Valeur par défaut
    email = models.EmailField(unique=True)
    Password = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.prenom} {self.nom} ({self.email})"

class PersonnelAdministratif(models.Model):
    email = models.EmailField(unique=True)
    Password = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.email} ({self.Password})"



class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"Message from {self.name} ({self.email})"