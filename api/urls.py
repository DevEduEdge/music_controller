from django.urls import path
from .views import main

urlpatterns = [
    # add path for web urls
    path('home',main),
    path('',main)
]
