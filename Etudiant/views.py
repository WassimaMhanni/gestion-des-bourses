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

def contactez_nous(request):
    return render(request, 'contactez-nous.html')

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




from django.shortcuts import render, redirect
from .forms import MessageForm
from django.contrib import messages

def contact(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Votre message a été envoyé avec succès !")
            messages.debug(request, "Débogage : Message envoyé avec succès !")

            return redirect('message_bien_envoye')  # Utilise le nom de l'URL définie dans urls.py
  # Redirige vers la page de contact ou une autre page après envoi*
        else:
            print(form.errors)  # Affiche les erreurs de validation dans la console
    else:
        form = MessageForm()

    return render(request, 'contactez-nous.html', {'form': form})
def message_bien_envoyer(request):
    return render(request, 'Messagebienenvoyer.html')

