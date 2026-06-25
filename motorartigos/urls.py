from django.urls import path
from motorartigos import views # ou 'from . import views' dependendo de onde o urls.py está

urlpatterns = [
    # A rota principal deve ter o name='home'
    path('', views.index, name='home'),
    
    # Já agora, garanta que a rota do detalhe do artigo também tem o nome correto:
    path('artigo/<int:id>/', views.artigo_detalhe, name='artigo_detalhe'),
]