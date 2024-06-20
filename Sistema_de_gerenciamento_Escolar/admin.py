from django.contrib import admin
from .models import Categoria_produto,Produtos
# Register your models here.

class Admin_Categoria_produto(admin.ModelAdmin):
    pass
@admin.register(Produtos)
class Admin_Produtos(admin.ModelAdmin): #Opção dois
    ...

admin.site.register(Categoria_produto,Admin_Categoria_produto)