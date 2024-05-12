from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
#from administrateur.forms import 
from restaurant.models import Restaurant, TypeResto, Commentaire
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, View, DeleteView


class administrateur(ListView):
    model = User
    template_name = 'administrateur.html'
    context_object_name = 'utilisateurs'

class supprimerUtilisateur(DeleteView):
    model = User
    template_name = 'supprimerUtilisateur.html'
    context_object_name = 'utilisateur'

    def get_success_url(self):
        return reverse('administrateur')
