from multiprocessing import context
from urllib.robotparser import RobotFileParser
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import formulaire_role
from .models import role
# Create your views here.
def index(request):
    return redirect('profils')




def details(request, role_id):
    id_role = role.objects.get(id = role_id)
    template = loader.get_template('jeu_role/details_profil.html')
    context = {
        'Nom': id_role.nom,
        'Race': id_role.race,
        'Classe': id_role.classe,
        'Niveau': id_role.niveau,
        'Equipement': id_role.equipement,
        'Partie': id_role.partie
    }
    return HttpResponse(template.render(context, request))

def profils(request):
    profils = role.objects.values('id', 'nom')
    context = {
        "profils": profils
    }
    return render(request,'jeu_role/profils.html',context)



def supprimer(request, role_id):
    id_role = role.objects.get(id = role_id)
    id_role.delete()
    return redirect('profils')


def creation_profils(request):
    if request.method =="POST":
        form = formulaire_role(request.POST).save()
        return redirect('creation_profils')
    else:
        form = formulaire_role()
    return render(request,'jeu_role/creation_profils.html', {'form' : form})

