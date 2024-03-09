import json

from redis import Redis

from django.conf import settings

class RedisTrabalhador:
    def __init__(self, host: str, porta: int, fila: int):
        self.redis = self.inicializa_redis(host, porta, fila)
        self.token = settings.CHAVE_SISTEMA,
        self.canal = settings.REDIS['CANAL_REDIS']

    def inicializa_redis(self, host: str, porta: int, fila: int) -> Redis:
        try:
            r = Redis(host=host, port=porta, db=fila)
            return r
        except:
            raise Exception

    def envia_mensagem(self, titulo: str, caminho: str) -> None:
        evento = {
            "titulo": titulo,
            "caminho_arquivo": caminho,
            "identificacao": self.token
        }
        mensagem_serializada = json.dumps(evento)
        self.redis.publish(self.canal, mensagem_serializada)
