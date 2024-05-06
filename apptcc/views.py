from django.shortcuts import render, redirect
from .models import Dispositivo, Scanner

def documentacao(request): 
#    numeros = range(1, 101)
#    link_base = '/admin/apptcc/dispositivo/add/?numero='  # Adicionando o marcador de posição para o número
#    return render(request, 'documentacao.html', {'numeros': numeros, 'link_base': link_base})
    endereco = Dispositivo.objects.all()
    return render(request, 'documentacao.html', {'endereco_ip' : endereco})
    
def home(request):
    bloco = Scanner.objects.count()
    return render(request, 'home.html',{
        'bloco' : bloco
    })

def servico(request):
    return render(request,'servicos.html')

def monitoramento(request):
    return render(request,'monitoramento.html')