from django.urls import path
from . import views

urlpatterns = [
    path('paises/', views.PaisListView.as_view(), name='pais_list'),
    path('paises/nuevo/', views.PaisCreateView.as_view(), name='pais_create'),
    path('paises/<int:pk>/', views.PaisUpdateView.as_view(), name='pais_update'),
    path('paises/<int:pk>/eliminar/', views.PaisDeleteView.as_view(), name='pais_delete'),
]
