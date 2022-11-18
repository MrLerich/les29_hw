from django.db import models

class Ad(models.Model):
    name = models.CharField(max_length=255, unique=True)
    author = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=400)
    address = models.CharField(max_length=300)
    is_published = models.BooleanField(default=True)

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)


