from django.urls import path, include
from administrateur.views import administrateur, supprimerUtilisateur

urlpatterns = [
    path('administrateur/', administrateur.as_view(), name='administrateur'),
    path('supprimerUtilisateur/<int:pk>/', supprimerUtilisateur.as_view(), name='supprimerUtilisateur'),
    path('consulterCommentaires/<int:pk>/', include('commentaire.urls')),
]