from produto.models import Produto
from django_filters import rest_framework as filters

class ProdutoFiltro(filters.FilterSet):
    titulo = filters.CharFilter(field_name='titulo', lookup_expr='icontains')
    # codigo = filters.CharFilter(field_name='codigo', lookup_expr='icontains')

    class Meta:
        model = Produto
        fields = ['codigo', 'titulo']
