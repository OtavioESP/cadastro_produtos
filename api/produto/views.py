import os
import redis

from django.conf import settings
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets, generics, views, status
from rest_framework.response import Response

from produto.models import Produto
from produto.filters import ProdutoFiltro
from produto.serializers import ProdutoSerializer, ProdutoFormulario, ProdutoAtualizaForm
from produto.utils.redis import RedisTrabalhador


class ProdutoView(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProdutoFiltro
    queryset = Produto.objects.all()
    lookup_field = 'codigo'

    def get_serializer_class(self):
        if self.action in ['partial_update', 'update']:
            return ProdutoAtualizaForm
        if self.action == 'create':
            return ProdutoFormulario
        return ProdutoSerializer


class ImportarArquivoView(views.APIView):
    def post(self, request, *args, **kwargs):
        '''
        A funçao é bem simples, receber o arquivo e
        gravar ele em um diretorio comum às aplicações
        '''
        arquivo = request.data.get('arquivo')
        caminho = os.path.join(os.path.dirname(os.getcwd()), 'importar_produtos', arquivo.name)

        with open(caminho, 'wb+') as arquivo_destino:
            for sessao in arquivo.chunks():
                arquivo_destino.write(sessao)

        redis = RedisTrabalhador(
            settings.REDIS['HOST_REDIS'],
            settings.REDIS['PORTA_REDIS'],
            settings.REDIS['FILA_REDIS'],
        )
        redis.envia_mensagem('importar_produtos', caminho)
        return Response({'mensagem': 'Arquivo enviado para processamento!'}, status=status.HTTP_200_OK)
