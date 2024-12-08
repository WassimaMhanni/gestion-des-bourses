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

def login_etd(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('Password')

        # Vérification dans la base de données
        try:
            etudiant = Etudiant.objects.get(email=email, Password=password)
            # Si l'étudiant existe, redirige vers une autre page
            return JsonResponse({'success': True, 'redirect_url': '/espace-etudiant/'})
        except Etudiant.DoesNotExist:
            # Affiche un message d'erreur si les informations ne sont pas correctes
            return JsonResponse({'success': False, 'message': 'Email ou mot de passe incorrect.'})

    return render(request, 'login.html')

def espace_etudiant(request):
    return render(request, 'espace_etudiant.html')
