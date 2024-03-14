from django.test import TestCase
from restaurant.views import MenuItemsView
from restaurant.models import Menu
from restaurant.serializers import menuSerializer
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

class MenuViewTest(TestCase):
    def setup(self):
        Menu.objects.create(id=6, title="Falafel", price=20, inventory=20)
        Menu.objects.create(id=7, title="Shawarma", price=40, inventory=50)
        
    def test_getall(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')
        url = reverse('menu') 
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        menus = Menu.objects.all()
        serializer = menuSerializer(menus, many=True)
        
        self.assertEqual(response.data, serializer.data)