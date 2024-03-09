import json

from os import getenv
from config.redis_config import conecta_ao_canal, inicializa_redis
from config.db_config import efetua_insercao


def comeco():
    host: str = getenv('HOST_REDIS', '')
    porta: int = getenv('PORTA_REDIS', 0000)
    fila: int = getenv('FILA_REDIS', 0)

    r = inicializa_redis(host=host, porta=porta, fila=fila)
    ouvinte = conecta_ao_canal(r,getenv('CANAL_REDIS', ''))

    for sinal in ouvinte.listen():
        if sinal['type'] == 'message':
            mensagem = sinal['data'].decode('utf-8')
            mensagem = json.loads(mensagem)
            if mensagem['titulo'] == 'importar_produtos':
                efetua_insercao(mensagem['caminho_arquivo'])
            print(f"Mensagem processada! {mensagem['titulo']}")
