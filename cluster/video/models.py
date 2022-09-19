from django.db import models

# Create your models here.

class Video(models.Model):
    video = models.FileField(upload_to="video", blank=False, null=False)
    poster_url = models.TextField(max_length=50, default="poster/video/default.jpg")
    name = models.TextField(max_length=40)
    size = models.FloatField()
