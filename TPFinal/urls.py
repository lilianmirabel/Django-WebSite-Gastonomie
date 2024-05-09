from django.contrib import admin
from django.urls import path, include
from TPFinal.views import *
from usagers.views import enregistrement
from django.contrib.auth import views as authentification_views


urlpatterns = [
    path('', accueilView.as_view(), name='accueil'),
    path('admin/', admin.site.urls),
    path('administrateur/', include('administrateur.urls')),
    path('restaurant/', include('restaurant.urls')),
    path('commentaire/', include('commentaire.urls')),
    path('enregistrement/',enregistrement, name='enregistrement'),
    path('login/', authentification_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', authentification_views.LogoutView.as_view(template_name='logged_out.html'), name='logout'),
]
