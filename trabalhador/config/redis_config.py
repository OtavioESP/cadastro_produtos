from redis import Redis

def inicializa_redis(host: str, porta: int, fila: int) -> Redis:
    try:
        r = Redis(host=host, port=porta, db=fila)
        return r
    except:
        raise Exception

def conecta_ao_canal(r: Redis, canal: str):
    try:
        ouvinte = r.pubsub()
        ouvinte.subscribe(canal)
        print(f'Redis inicializado com sucesso !\nOuvindo ao canal: => {canal}')
        return ouvinte
    except:
        raise Exception
