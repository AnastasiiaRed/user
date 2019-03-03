from django.test import TestCase
from user1.views import login
from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TransactionTestCase, Client
from  django.shortcuts import redirect

from django.contrib.auth import authenticate


class TestSuite(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='jacob@mzil.tu')
        self.user.save()

    def test_secure_page(self):
        self.c = Client()
        self.user = authenticate(username='user', password='hello') 
        login = self.c.login(username='user', password='hello') 
        self.assertTrue(login)
		
    def test_secure_page_1(self):
        self.c = Client()
        self.user = authenticate(username='', password='hello') 
        login = self.c.login(username='', password='hello') 
        self.assertTrue(login)
		
    def test_secure_page_2(self):
        self.c = Client()
        self.user = authenticate(username='testuser', password='he') 
        login = self.c.login(username='testuser', password='he') 
        self.assertTrue(login)