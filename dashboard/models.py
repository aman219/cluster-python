from django.db import models

# Create your models here.

class Visited(models.Model):
    count = models.PositiveIntegerField(default=0)
    time = models.DateField(auto_now_add=True)
