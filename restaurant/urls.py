from django.urls import path, include
from restaurant.views import ajoutTypeRestaurant, ajoutRestaurant, listeRestaurant, detailRestaurant, modifierRestaurant, supprimerRestaurant

urlpatterns = [
    path('ajoutTypeRestaurant/', ajoutTypeRestaurant.as_view(), name='ajoutTypeRestaurant'),
    path('ajoutRestaurant/', ajoutRestaurant.as_view(), name='ajoutRestaurant'),
    path('listeRestaurant/', listeRestaurant.as_view(), name='listeRestaurant'),
    path('detail/<int:pk>/', detailRestaurant.as_view(), name='detailRestaurant'),
    path('modifierRestaurant/<int:pk>/', modifierRestaurant.as_view(), name='modifierRestaurant'),
    path('supprimerRestaurant/<int:pk>/', supprimerRestaurant.as_view(), name='supprimerRestaurant'),
    path('ajouterCommentaire/<int:pk>/', include('commentaire.urls')),
]