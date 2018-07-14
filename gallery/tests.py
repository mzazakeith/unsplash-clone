from django.test import TestCase
from .models import Image, Category, Location


class LocationTestClass(TestCase):

    def setUp(self):
        self.africa = Location(location='Africa')

    def test_instance(self):
        self.assertTrue(isinstance(self.africa, Location))

    def test_save_method(self):
        self.africa.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)


