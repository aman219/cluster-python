from unicodedata import name
from django.urls import path
from . import views
urlpatterns =[
    path('', views.video, name="video"),
    path('<int:id>/', views.svideo, name="svideo"),
    path('delete/<int:id>/', views.deleteVideo, name="deleteVideo")
]