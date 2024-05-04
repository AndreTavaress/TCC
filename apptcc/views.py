from django.shortcuts import render, redirect
from .models import Dispositivo, Offline

def documentacao(request): 
#    numeros = range(1, 101)
#    link_base = '/admin/apptcc/dispositivo/add/?numero='  # Adicionando o marcador de posição para o número
#    return render(request, 'documentacao.html', {'numeros': numeros, 'link_base': link_base})
    endereco = Offline.objects.all()
    return render(request, 'documentacao.html', {'endereco_ip' : endereco})
    
def home(request):
    return render(request, 'home.html')