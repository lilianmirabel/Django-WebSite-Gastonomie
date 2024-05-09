from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from commentaire.forms import ajouterCommentaireForm
from restaurant.models import Restaurant, TypeResto, Commentaire
from datetime import datetime, timedelta
from django.urls import reverse
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
