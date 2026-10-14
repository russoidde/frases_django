from django.urls import path
from .import views
from .views import (
    FraseCreateView,
    FraseDeleteView,
    FraseListView,
    FraseNoVisibleListView,
    FraseVisibleListView,
    FraseUpdateView

)

app_name = 'frases'


urlpatterns = [
    path('listar/', views.FraseListView.as_view(), name='listar'),
    path('crear/', views.FraseCreateView.as_view(), name='crear'),
    path('modificar/<int:pk>/', views.FraseUpdateView.as_view(), name='modificar'),
    path('borrar/<int:pk>/', views.FraseDeleteView.as_view(), name='borrar'),
    path('detalle_frase/<int:pk>/', views.detalle_frase, name='detalle_frase'),
    path('modificar_activo/<int:pk>/', views.modificar_activo, name='modificar_activo'),
    path('visibles/', views.FraseVisibleListView.as_view(), name='frases_visibles'),
    path('no_visibles/', views.FraseNoVisibleListView.as_view(), name='frases_no_visibles'),
    path('listar_json', views.listar_Json, name='listar_json')

]