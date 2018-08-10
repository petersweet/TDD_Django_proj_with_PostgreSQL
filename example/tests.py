from django.test import TestCase
from django.test import Client

# Create your tests here.

class TestNavigations(TestCase):

    def setUp(self):
        self.client = Client()

    def home_test(self):
        homepage = self.client.get('^')
        self.assertTrue(homepage.responce, 200)
        self.assertTemplateUsed(homepage, 'home.html')
