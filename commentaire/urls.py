from django.urls import path, include
from commentaire.views import ajouterCommentaire, ListeCommentaires, modifierCommentaire, supprimerCommentaire, consulterCommentaires

urlpatterns = [
    path('ajouterCommentaire/<int:pk>/', ajouterCommentaire.as_view(), name='ajouterCommentaire'),
    path('ListeCommentaires/', ListeCommentaires.as_view(), name='ListeCommentaires'),
    path('modifierCommentaire/<int:pk>/', modifierCommentaire.as_view(), name='modifierCommentaire'),
    path('supprimerCommentaire/<int:pk>/', supprimerCommentaire.as_view(), name='supprimerCommentaire'),
    path('consulterCommentaires/<int:pk>/', consulterCommentaires.as_view(), name='consulterCommentaires'),
]