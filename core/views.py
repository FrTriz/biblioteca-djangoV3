from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from core.filters import LivroFilter
from .models import Livro, Autor, Categoria
from .serializers import LivroSerializer, AutorSerializer, CategoriaSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import LivroFilter

# Lista e criação de livros
class LivroList(generics.ListCreateAPIView):
    queryset = Livro.objects.all()  # Todos os livros
    serializer_class = LivroSerializer  # Serializador para os livros
    filterset_class = LivroFilter  # Filtro personalizado para livros
    search_fields = ['titulo', 'autor__nome', 'categoria__nome']  # Filtros de busca
    ordering_fields = ['titulo', 'autor', 'categoria', 'publicado_em']  # Campos disponíveis para ordenação
    ordering = ['titulo']  # Ordenação padrão (título)

# Detalhes, atualização e deleção de livros
class LivroDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Livro.objects.all()  # Seleciona todos os livros
    serializer_class = LivroSerializer  # Serializer para os livros
    name = "livro-detail"  # Nome da view

# Lista e criação de categorias
class CategoriaList(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()  # Seleciona todas as categorias
    serializer_class = CategoriaSerializer  # Serializer para categorias

# Detalhes, atualização e deleção de categorias
class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()  # Seleciona todas as categorias
    serializer_class = CategoriaSerializer  # Serializer para categorias

# Lista e criação de autores
class AutorList(generics.ListCreateAPIView):
    queryset = Autor.objects.all()  # Seleciona todos os autores
    serializer_class = AutorSerializer  # Serializer para autores

# Detalhes, atualização e deleção de autores
class AutorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()  # Seleciona todos os autores
    serializer_class = AutorSerializer  # Serializer para autores

from rest_framework import generics, permissions
from .models import Colecao
from .serializers import ColecaoSerializer
from .permissions import IsOwnerOrReadOnly

class ColecaoListCreate(generics.ListCreateAPIView):
    queryset = Colecao.objects.all()
    serializer_class = ColecaoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(colecionador=self.request.user)

class ColecaoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Colecao.objects.all()
    serializer_class = ColecaoSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
