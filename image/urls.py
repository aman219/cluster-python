from django.urls import path
from . import views

urlpatterns =[
    path("", views.image, name="image"),
    path("delete/<int:id>/", views.deleteImage, name="deleteImage")
]