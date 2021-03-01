from django.core.validators import MinValueValidator
from django.db import models


class Produto(models.Model):
    class Meta:
        verbose_name_plural = "Produtos"

    descricao = models.CharField(verbose_name="Descrição", max_length=50)
    data_validade = models.DateField(verbose_name="Data de validade")
    data_cadastro = models.DateField(verbose_name="Data de cadastro", auto_now_add=True)
    data_atualizacao = models.DateTimeField(verbose_name="Data de atualização", auto_now=True)
    qtd_estoque = models.IntegerField(verbose_name="Quantidades/Unid em estoque", validators=[MinValueValidator(1)])
    preco_unid = models.DecimalField(verbose_name="Preço da Unidade",max_digits=20, decimal_places=2)

    def __str__(self):
        return self.descricao