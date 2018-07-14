from django.db import models


class Location(models.Model):
    location = models.CharField(max_length=30)

    def __str__(self):
        return self.location

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()


