from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns = [
    path('paises/', views.PaisListView.as_view(), name='pais_list'),
    path('paises/nuevo/', views.PaisCreateView.as_view(), name='pais_create'),
    path('paises/<int:pk>/', views.PaisUpdateView.as_view(), name='pais_update'),
    path('paises/<int:pk>/eliminar/', views.PaisDeleteView.as_view(), name='pais_delete'),
    path('departamentos/', views.DepartamentoListView.as_view(), name='departamento_list'),
    path('departamentos/nuevo/', views.DepartamentoCreateView.as_view(), name='departamento_create'),
    path('departamentos/<int:pk>/', views.DepartamentoUpdateView.as_view(), name='departamento_update'),
    path('departamentos/<int:pk>/eliminar/', views.DepartamentoDeleteView.as_view(), name='departamento_delete'),
    path('municipios/', views.MunicipioListView.as_view(), name='municipio_list'),
    path('municipios/nuevo/', views.MunicipioCreateView.as_view(), name='municipio_create'),
    path('municipios/<int:pk>/', views.MunicipioUpdateView.as_view(), name='municipio_update'),
    path('municipios/<int:pk>/eliminar/', views.MunicipioDeleteView.as_view(), name='municipio_delete'),
]
