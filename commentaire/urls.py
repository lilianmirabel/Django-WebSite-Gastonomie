from django.urls import path
from commentaire.views import ajouterCommentaire

urlpatterns = [
    path('ajouterCommentaire/<int:pk>/', ajouterCommentaire.as_view(), name='ajouterCommentaire'),
]