from django.contrib import admin
from registro.models import (
    Funcionario, ColetaFaces, Treinamento, RegistroFuncionario)
 
class ColetaFacesInline(admin.StackedInline): 
    model = ColetaFaces
    extra = 0

class FuncionarioAdmin(admin.ModelAdmin):
    readonly_fields = ['slug']
    inlines = (ColetaFacesInline,) 
    
admin.site.register(Funcionario, FuncionarioAdmin)

# admin.site.register(Funcionario)
# admin.site.register(ColetaFaces) 

admin.site.register(Treinamento)

admin.site.register(RegistroFuncionario)