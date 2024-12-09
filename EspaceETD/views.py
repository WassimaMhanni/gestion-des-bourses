
from django.shortcuts import render
from django.http import HttpResponse
#la en meme  les fonctions suad  on utilise
from django.shortcuts import render, redirect
from django.contrib import messages
#from .models import Etudiant
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
#from .models import Etudiant  # Modèle représentant les étudiants

from django.http import JsonResponse

from Etudiant.models import Etudiant





# Vue pour l'espace étudiant
def espace_etudiant_view(request):
    # Récupérer les informations de l'étudiant depuis la session
    etudiant_nom = request.session.get('etudiant_nom', 'Inconnu')
    etudiant_prenom = request.session.get('etudiant_prenom', 'Inconnu')

    context = {
        'nom': etudiant_nom,
        'prenom': etudiant_prenom,
    }
    return render(request, 'espace_etudiant.html', context)



# views.py
from django.shortcuts import render, redirect
from .forms import DossierDeCandidatureForm  # Importer le formulaire

def formulaire_candidature(request):
    if request.method == 'POST':
        form = DossierDeCandidatureForm(request.POST, request.FILES)
        if form.is_valid():  # Vérifie si le formulaire est valide
            form.save()  # Enregistre les données dans la base de données
            return redirect('confirmation_page.html')  # Redirige vers une page de confirmation
    else:
        form = DossierDeCandidatureForm()  # Formulaire vide si la méthode est GET

    return render(request, 'formulaire.html', {'form': form})

def confirmation_formulaire(request):
    return render(request, 'confirmation_page.html')  # Créez un fichier success.html


