from django.urls import path
from commentaire.views import ajouterCommentaire, ListeCommentaires, modifierCommentaire, supprimerCommentaire

urlpatterns = [
    path('ajouterCommentaire/<int:pk>/', ajouterCommentaire.as_view(), name='ajouterCommentaire'),
    path('ListeCommentaires/', ListeCommentaires.as_view(), name='ListeCommentaires'),
    path('modifierCommentaire/<int:pk>/', modifierCommentaire.as_view(), name='modifierCommentaire'),
    path('supprimerCommentaire/<int:pk>/', supprimerCommentaire.as_view(), name='supprimerCommentaire'),
]