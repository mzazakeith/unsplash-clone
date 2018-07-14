from django.db import models


class Location(models.Model):
    location = models.CharField(max_length=30)

    def __str__(self):
        return self.location

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()


class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()


class Image(models.Model):
    image_name = models.CharField(max_length=50)
    image_description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    image_link = models.CharField(max_length=500)
    categories = models.ForeignKey(Category)
    location = models.ForeignKey(Location)

    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def show_images(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def search_image(cls, category):
        images = cls.objects.filter(image_description__icontains=category)

        return images

    @classmethod
    def filter_by_location(cls, id):
        images = cls.objects.filter(location_id=id)
        return images
