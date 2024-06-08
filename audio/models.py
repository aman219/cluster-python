from unicodedata import name
from django.db import models

# Create your models here.

class Audio(models.Model):
    name = models.TextField(max_length=50)
    audio_file = models.FileField(upload_to="audio", blank=False, null=False)