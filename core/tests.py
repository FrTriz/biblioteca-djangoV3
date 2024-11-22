from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Colecao

class ColecaoTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

    def test_create_colecao(self):
        data = {'nome': 'Minha Coleção', 'descricao': 'Descrição da coleção'}
        response = self.client.post('/colecoes/', data)  # URL para criar coleção
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Colecao.objects.count(), 1)
