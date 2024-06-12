from django.urls import path
from . import views

urlpatterns =[
    path('', views.audio, name="audio"),
    path('<int:id>/', views.paly, name="play"),
    path('delete/<int:id>/', views.deleteAudio, name="deleteAudio")
]