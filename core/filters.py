from django_filters import rest_framework as filters
from .models import Livro

class LivroFilter(filters.FilterSet):
    titulo = filters.CharFilter(lookup_expr='icontains')  # Filtro para o título (case insensitive)
    autor = filters.CharFilter(field_name='autor__nome', lookup_expr='icontains')  # Filtro para autor
    categoria = filters.AllValuesFilter(field_name='categoria__nome')  # Filtro para categoria (todos os valores)
    
    class Meta:
        model = Livro
        fields = ['titulo', 'autor', 'categoria']  # Campos disponíveis para filtragem
