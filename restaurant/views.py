from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from restaurant.forms import ajoutTypeRestaurantForm, ajoutRestaurantForm
from .models import Restaurant, TypeResto, Commentaire
from datetime import datetime, timedelta
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, View, DeleteView


class ajoutTypeRestaurant(CreateView):
  template_name = 'ajoutTypeRestaurant.html'
  form_class = ajoutTypeRestaurantForm

  def get_success_url(self):
      return reverse('accueil')

  def form_valid(self, form):
        form.save()
        return super().form_valid(form)

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context["txtBouton"] = 'Ajouter'
      return context

class ajoutRestaurant(CreateView):
  template_name = 'ajoutRestaurant.html'
  form_class = ajoutRestaurantForm

  def get_success_url(self):
      return reverse('accueil')

  def form_valid(self, form):
        form.save()
        return super().form_valid(form)

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context["txtBouton"] = 'Ajouter'
      return context

class listeRestaurant(ListView):
    model = Restaurant
    template_name = 'listeRestaurant.html'
    context_object_name = 'restaurants'

class detailRestaurant(DetailView):
    model = Restaurant
    template_name = 'detailRestaurant.html'
    context_object_name = 'restaurant'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['commentaires'] = Commentaire.objects.filter(noRestaurant=self.object)
        return context

class modifierRestaurant(UpdateView):
    model = Restaurant
    template_name = 'modifierRestaurant.html'
    form_class = ajoutRestaurantForm
    context_object_name = 'restaurant'

    def get_success_url(self):
        return reverse('listeRestaurant')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["txtBouton"] = 'Modifier'
        return context

class supprimerRestaurant(DeleteView):
    model = Restaurant
    template_name = 'supprimerRestaurant.html'
    context_object_name = 'restaurant'

    def get_success_url(self):
        return reverse('listeRestaurant')
