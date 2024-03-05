from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validar_nao_zero(valor: int):
    if valor == 0:
        raise ValidationError(_("Valor não pode ser menor ou igual a 0"), params={"valor": valor})
