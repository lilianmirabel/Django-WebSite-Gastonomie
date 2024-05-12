from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from restaurant.forms import ajoutTypeRestaurantForm, ajoutRestaurantForm, RestaurantFilterForm
from .models import Restaurant, TypeResto, Commentaire
from datetime import datetime, timedelta
from django.db.models import Avg
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, View, DeleteView


class ajoutTypeRestaurant(CreateView):
  template_name = 'ajoutTypeRestaurant.html'
  form_class = ajoutTypeRestaurantForm

  def get_success_url(self):
      return reverse('listeRestaurant')

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
      return reverse('listeRestaurant')

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

    def get_queryset(self):
        queryset = super().get_queryset()
        form = RestaurantFilterForm(self.request.GET)
        if form.is_valid():
            nom = form.cleaned_data.get('nom')
            ville = form.cleaned_data.get('ville')
            type = form.cleaned_data.get('type')
            if nom:
                queryset = queryset.filter(nomRestaurant__icontains=nom)
            if ville:
                queryset = queryset.filter(villeRestaurant__icontains=ville)
            if type:
                queryset = queryset.filter(typeRestaurant=type)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = RestaurantFilterForm(self.request.GET)
        return context

class detailRestaurant(DetailView):
    model = Restaurant
    template_name = 'detailRestaurant.html'
    context_object_name = 'restaurant'
    
    def get_context_data(self, **kwargs):
        unCommentaire = self.get_object()
        context = super().get_context_data(**kwargs)
        context['commentaires'] = Commentaire.objects.filter(noRestaurant=self.object)
        
        if self.request.user.is_authenticated:
            commentaire_exist = Commentaire.objects.filter(noRestaurant=unCommentaire, userName=self.request.user).exists()
            context['commentaire_exist'] = commentaire_exist
        else:
            context['commentaire_exist'] = False
        
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
