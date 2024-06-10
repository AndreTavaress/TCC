from django.shortcuts import render, redirect

from .models import Dispositivo, Scanner, Service, Offline
from apptcc.management.comands.scan_tempo import check_cidr_block 
from django.core.cache import cache
from .models import Dispositivo

CACHE_KEY_OFFLINE = 'offline_ips'

def documentacao(request): 
    scan = Scanner.objects.all()
    off = Offline.objects.all()
        
    if request.method == 'POST':
        check_cidr_block(request.POST.get('selected_ip'))
        return render(request, 'documentacao.html', {'off' : off})

    return render(request, 'documentacao.html', {'scan': scan})
    
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
