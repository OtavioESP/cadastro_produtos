from produto.models import Produto
from rest_framework import serializers


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'

class ProdutoForm(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'
