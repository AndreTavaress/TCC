from django.shortcuts import render, redirect
from .models import Dispositivo

def documentacao(request): 
    numeros = range(1, 101)
    link_base = '/admin/apptcc/dispositivo/add/?numero='  # Adicionando o marcador de posição para o número
    return render(request, 'documentacao.html', {'numeros': numeros, 'link_base': link_base})
    
def adicionar_dispositivo(request):
    numero = request.GET.get('numero')
    if numero:
        dispositivo = Dispositivo.objects.create(ip=numero)
        # Redirecionar para a página de adição de dispositivo, passando o número como parâmetro
        return redirect('/admin/apptcc/dispositivo/add/?numero=' + numero)
    
def home(request):
    return render(request, 'home.html')