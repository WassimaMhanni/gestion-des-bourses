from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#la en meme  les fonctions suad  on utilise
def home (request ) :
    return render(request,'home.html')
def login(request):
    return render(request,'login.html')
def register(request):
    return render(request,'register.html')
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Etudiant

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Etudiant  # Modèle représentant les étudiants


from django.http import JsonResponse


# Vue de connexion
def login_etd(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('Password')

        try:
            # Vérifier si l'étudiant existe dans la base de données
            etudiant = Etudiant.objects.get(email=email, Password=password)

            # Stocker les informations dans la session
            request.session['etudiant_id'] = etudiant.id  # Stocker l'ID
            request.session['etudiant_nom'] = etudiant.nom
            request.session['etudiant_prenom'] = etudiant.prenom

            # Rediriger vers l'espace étudiant
            return JsonResponse({'success': True, 'redirect_url': '/espace_etudiant/'})

        except Etudiant.DoesNotExist:
            # Si les informations ne sont pas valides
            return JsonResponse({'success': False, 'message': 'Email ou mot de passe incorrect.'})

    return render(request, 'login.html')
#def espace_etudiant(request):
    #return render(request, 'espace_etudiant.html')
