from django.db import models

# Create your models here.

class File (models.Model):
    file = models.FileField(upload_to='file', blank=True, null=True)
    name = models.TextField(max_length=50)