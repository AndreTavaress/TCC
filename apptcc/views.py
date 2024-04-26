from django.shortcuts import render, redirect
from .models import Dispositivo, Scanner

def documentacao(request): 
    address_bloco = Scanner.objects.all()
    return render(request, 'documentacao.html', {
        'address_bloco' : address_bloco
        })

    
def home(request):
    return render(request, 'home.html')
