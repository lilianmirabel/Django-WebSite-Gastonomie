from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.views.generic import TemplateView

class accueilView(TemplateView):
  template_name = 'accueil.html'
