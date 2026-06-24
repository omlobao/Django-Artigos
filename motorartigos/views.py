from django.shortcuts import render


def index(request):
    return render(request, 'motorartigos/index.html')

def artigo(request):
    return render(request, 'motorartigos/artigos.html')
