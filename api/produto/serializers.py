from rest_framework import serializers

from .models import Produto


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'

class ProdutoFormulario(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = [
            'codigo',
            'titulo',
            'preco',
        ]

class ProdutoAtualizaForm(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = [
            'titulo',
            'preco',
        ]
