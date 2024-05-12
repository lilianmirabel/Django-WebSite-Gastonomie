from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from commentaire.forms import ajouterCommentaireForm, modifierCommentaireForm
from restaurant.models import Restaurant, TypeResto, Commentaire
from datetime import datetime, timedelta
from django.urls import reverse
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, View, DeleteView

class ajouterCommentaire(CreateView):
  template_name = 'ajouterCommentaire.html'
  form_class = ajouterCommentaireForm

  def get_success_url(self):
      return reverse('listeRestaurant')  


  def form_valid(self, form):
      restaurant_id = self.kwargs['pk']
      restaurant = Restaurant.objects.get(pk=restaurant_id)
      user = self.request.user
      form.instance.noRestaurant = restaurant
      form.instance.userName = user
      return super().form_valid(form)
      

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context["txtBouton"] = 'Ajouter'
      return context

class ListeCommentaires(ListView):
    model = Commentaire
    template_name = 'listeCommentaires.html'
    context_object_name = 'commentaires'

    def get_queryset(self):
        user = self.request.user
        return Commentaire.objects.filter(userName=user)

class modifierCommentaire(UpdateView):
    model = Commentaire
    template_name = 'modifierCommentaire.html'
    form_class = modifierCommentaireForm
    context_object_name = 'unCommentaire'

    def get_success_url(self):
        return reverse('listeRestaurant')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["txtBouton"] = 'Modifier'
        return context

class supprimerCommentaire(DeleteView):
    model = Commentaire
    template_name = 'supprimerCommentaire.html'
    context_object_name = 'unCommentaire'

    def get_success_url(self):
        return reverse('listeRestaurant')

class consulterCommentaires(ListView):
    model = Commentaire
    template_name = 'consulterCommentaires.html'
    context_object_name = 'lesCommentaires'

    def get_queryset(self):
        id = self.kwargs.get('pk')
        user = User.objects.get(id=id)
        return Commentaire.objects.filter(userName=user)
