from django.contrib import admin
from apptcc.models import Scanner, Dispositivo, Service
from apptcc.management.comands.scan import main as scan_main
from apptcc.management.comands.service import scan_ports

@admin.action(description="Executar Scanner")
def executar_scanner(modeladmin, request, queryset):
    for item in queryset:
        if item.ativo.lower() == 'sim':
            rede = item.rede
            mascara = item.mascara
            scan_main(rede, mascara)
            
        else:
            modeladmin.error(request, "Bloco IP selecionado se encontra desativado!")
 
    modeladmin.message_user(request, f"Scanner executado com sucesso para {queryset.count()} itens.")



@admin.register(Scanner)
class ScannerAdmin(admin.ModelAdmin):
    list_display = ('rede', 'mascara','ativo',)
    list_editable = ('ativo',)
    actions = [executar_scanner,]

@admin.action(description="Varredura de portas")
def executar_service(modeladmin, request, queryset):
    for ip in queryset:
        disp = ip
        scan_ports(disp)

@admin.register(Dispositivo)
class DispositivoAdmin(admin.ModelAdmin):
    list_display = ('ip','nome_do_dispositivo','status',)
    actions = [executar_service,]
    
    
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('dispositivo',"lista_de_coisas",)