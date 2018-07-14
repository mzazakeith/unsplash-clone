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


class CategoryTestClass(TestCase):

    def setUp(self):
        self.abstract = Category(category_name="abstract")

    def test_instance(self):
        self.assertTrue(isinstance(self.abstract, Category))

    def test_save_method(self):
        self.abstract.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_delete_method(self):
        self.abstract.save_category()
        self.abstract.delete_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) == 0)


class ImageTestClass(TestCase):
    def setUp(self):
        self.africa = Location(location='Africa')
        self.africa.save_location()

        self.abstract = Category(category_name="abstract")
        self.abstract.save_category()

        self.new_image = Image(image_name='Test Image', image_description='An abstract image taken in africa',
                               image='image/example.jpg', image_link='google.com/image/1', categories=self.abstract,
                               location=self.africa)

        self.new_image.save()

    def tearDown(self):
        Location.objects.all().delete()
        Category.objects.all().delete()
        Image.objects.all().delete()

    def test_show_images(self):
        images = Image.show_images()
        self.assertTrue(len(images) > 0)
