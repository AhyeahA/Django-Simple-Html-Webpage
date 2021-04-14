
from django.urls import path
from .import views

urlpatterns = [
    path("", views.displayMenu, name = "menu"),
    
]