from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # Rotas para livros
    path('livros/', views.LivroList.as_view(), name='livros-list'),  # Listar e criar livros
    path('livros/<int:pk>/', views.LivroDetail.as_view(), name='livro-detail'),  # Detalhar, atualizar ou deletar livro

    # Rotas para categorias
    path('categorias/', views.CategoriaList.as_view(), name='categorias-list'),  # Listar e criar categorias
    path('categorias/<int:pk>/', views.CategoriaDetail.as_view(), name='categoria-detail'),  # Detalhar, atualizar ou deletar categoria

    # Rotas para autores
    path('autores/', views.AutorList.as_view(), name='autores-list'),  # Listar e criar autores
    path('autores/<int:pk>/', views.AutorDetail.as_view(), name='autor-detail'),  # Detalhar, atualizar ou deletar autor

    path('colecoes/', views.ColecaoListCreate.as_view(), name='colecoes-list-create'),
    path('colecoes/<int:pk>/', views.ColecaoDetail.as_view(), name='colecoes-detail'),

    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns += [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

