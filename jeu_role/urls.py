from django.urls import path

from . import views

urlpatterns = [
    path('', views.profils, name='profils'),
    path('profils', views.profils, name='profils'),
    path('supprimer/<int:role_id>', views.supprimer, name="supprimer"),
    path('creation_profils', views.creation_profils, name='creation_profils'),
    path('details/<int:role_id>', views.details, name='details')
]