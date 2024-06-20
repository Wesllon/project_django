from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Categoria_produto(models.Model):
        nome_categoria = models.CharField(max_length=50)
        def __str__(self) -> str:
          return  self.nome_categoria

class Produtos(models.Model):
    nome_produto = models.CharField(max_length=40)
    quantidade_produto = models.IntegerField()
    valor_produto = models.FloatField()
    data_vencimento = models.DateField(auto_now_add=True)
    img_produto = models.ImageField(upload_to='Sistema_de_gerenciamento_Escolar/images/%Y/%m/%d/')
    categoria = models.ForeignKey(Categoria_produto,on_delete= models.SET_NULL,null=True)
    dono = models.ForeignKey(User,on_delete= models.SET_NULL,null=True)