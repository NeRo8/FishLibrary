from django.db import models


# Create your models here.
class Fishes(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    avatar = models.ImageField(upload_to='fishes')

    def __str__(self):
        return self.title
