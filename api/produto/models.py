from django.db import models

from produto.validators import validar_nao_zero


class Produto(models.Model):
    codigo = models.IntegerField(unique=True)
    titulo = models.CharField(
        max_length=200, validators=[validar_nao_zero])
    preco = models.DecimalField(
        decimal_places=2,
        max_digits=8,
        validators=[validar_nao_zero]
    )

    def __str__(self):
        return f'#{self.codigo} - {self.titulo} - R${self.preco}'
