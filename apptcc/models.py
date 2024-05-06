from typing import Any
from django.db import models
import json

class Scanner(models.Model):
    choices = (('sim','Sim'),
               ('não','Não'))   
    rede = models.CharField(max_length = 16)
    mascara = models.CharField(max_length = 3)
    ativo = models.CharField(max_length = 3, choices=choices)

    def __str__ (self):
        return (self.rede+'\n'+self.mascara)  
    
class Dispositivo(models.Model):
    ip = models.CharField(max_length = 16)
    nome_do_dispositivo = models.CharField(max_length=100)
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"IP: {self.ip} - Nome do dispositivo: {self.nome_do_dispositivo}"
    
class Service(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE, null=True, blank=True)
    lista_de_coisas = models.TextField(blank=True, null=True)

    def salvar_lista(self, lista):
        self.lista_de_coisas = json.dumps(lista)
        self.save()

    def obter_lista(self):
        if self.lista_de_coisas:
            return json.loads(self.lista_de_coisas)
        else:
            return []

    def __str__(self):
        return f"Dispositivo IP: {self.dispositivo} - Lista de serviços: {self.lista_de_coisas}"

