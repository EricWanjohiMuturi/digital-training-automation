from django.urls import path
from .views import training

urlpatterns = [
    path('', training, name="home")
]