from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from produto.models import Produto
from produto.filters import ProdutoFiltro
from produto.serializers import ProdutoSerializer, ProdutoForm


class ProdutoView(ModelViewSet):
    queryset = Produto.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProdutoFiltro
    lookup_field = 'codigo'

    def get_serializer_class(self):
        if self.action in ['update', 'create']:
            return ProdutoForm
        return ProdutoSerializer
