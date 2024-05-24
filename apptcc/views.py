from django.shortcuts import render, redirect

from .models import Dispositivo, Scanner, Service

from .models import Dispositivo

def documentacao(request): 
#    numeros = range(1, 101)
#    link_base = '/admin/apptcc/dispositivo/add/?numero='  # Adicionando o marcador de posição para o número
#    return render(request, 'documentacao.html', {'numeros': numeros, 'link_base': link_base})

    endereco = Dispositivo.objects.all()
    scan = Scanner.objects.all()
    return render(request, 'documentacao.html', {'endereco_ip' : endereco,
                                                 'scan' : scan})
    
def home(request):
    endereco = Dispositivo.objects.count()
    bloco = Scanner.objects.count()
    return render(request, 'home.html',{
        'bloco' : bloco,
        'endereco' : endereco
    })

def servico(request):
    service = Service.objects.all()
    return render(request,'servicos.html', {
        'service' : service
    })

def monitoramento(request):
    dispositivo = Dispositivo.objects.all()
    return render(request,'monitoramento.html', {
        'dispositivo' : dispositivo
    })
