from django.test import TestCase
from .models import Property

class PropertyPostRequest(TestCase):
    def fakeData(self):
        Property.objects.create()
