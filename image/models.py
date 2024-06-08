from django.db import models

# Create your models here.

class Image (models.Model):
    name = models.TextField(max_length=30)
    image = models.ImageField(upload_to='image')
