from unicodedata import name
from xml.etree.ElementInclude import include
from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload, name='upload')
]