from django.urls import path

# My Project
from src.index.views import index

# Default URL Patterns
urlpatterns = [
    path("", index, name="index"),
]