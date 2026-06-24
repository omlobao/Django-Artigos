from django.urls import path
from .views import artigo

urlpatterns = [
    path('', artigo, name='home'),
    path('artigo/', artigo, name='artigo'),
]