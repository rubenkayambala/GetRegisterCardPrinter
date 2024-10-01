from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import CarteForm
from .models import Carte

def HomeView(request):
    template_name = 'home/index.html'
    return render(request, template_name)


def RegisterView(request):
    template_name = 'home/register.html'
    if request.method == "POST":
        form = CarteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/list/')
        else:
            messages.error(request, "Données incorrectes! Réessayez")
            form = CarteForm()
            context = {
                'form': form,
            }
            return render(request, template_name, context)
    form = CarteForm()
    context = {
        'form': form,
    }
    return render(request, template_name, context)


def ListView(request):
    users = Carte.objects.all()
    template_name = 'home/list.html'
    context = {
        'users': users,
    }
    return render(request, template_name, context)


def DetailView(request, id):
    user = Carte.objects.get(id=id)
    template_name = 'home/detail.html'
    context = {
        'user': user,
    }
    return render(request, template_name, context)
