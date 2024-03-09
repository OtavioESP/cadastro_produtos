# cadastro_produtos

Um projeto de teste técnico para cadastro de produtos.

# Requisitos do projeto:

## Python 3.8.x

## Postman ou algum aplicativo para envio de requisicoes HTTP

## Docker

Para começar o projeto, precisaremos de 4 terminais

Lembrnado que para o perfeito funcionamento, as variaveis de ambiente:
export CHAVE_SISTEMA=""

BD_NOME
BD_USUARIO
BD_SENHA
BD_HOST
BD_PORTA
CANAL_REDIS
HOST_REDIS
PORTA_REDIS
FILA_REDI

Devem em todas as instâncias que são criadas, possuir os mesmos valores.

Em visão de nao expor os valores das variáveis a publico, elas são enviadas em um arquivo separado junto ao link do github do teste.

# 1 - BANCO DE DADOS

Primeiro você irá entrar em:

```
$ cd postgres
$ docker-compose up -d

O docker se encarregará de criar o banco de dados chamado 'produtos_db' automaticamente com certas variaveis de conexao
```

# 2 - DJANGO API

```
$ cd api

Agora utilizando workon ou o python crie seu ambiente virtual
para o pyenv virtualenvwrapper use:
$ mkvirtualenv api

ou para o python:
$ python -m venv env
$ source env/bin/activate

Após ambiente criado rode:
$ pip install -r requirements.txt

$ python manage.py migrate
$ python manage.py createsuperuser

O terminal irá guiar para criar o superusuario.

Emfim:
$ python manage.py runserver

Utilize a sua melhor opçao para a exportacao de variaveis de ambiente
$ touch .envrc
ou
$ touch .env
Após gerado as variaveis de ambiente, voce deve inserir as seguintes variaveis

export DEBUG=True
export SECRET_KEY=""
export CHAVE_SISTEMA=""

export BD_NOME=""
export BD_USUARIO=""
export BD_SENHA=""
export BD_HOST=""
export BD_PORTA=""

export CANAL_REDIS=""
export HOST_REDIS=""
export PORTA_REDIS=6379
export FILA_REDIS=0

export ACCESS_TOKEN_LIFETIME=15
export REFRESH_TOKEN_LIFETIME=15

```

O Django REST possui um servico de interface para interagir com os dados.

Lembrando que, essa interface, pode ser acessada por usuarios administradores e
possui um acesso livre ao banco.

Para tal acesse:
localhost:8000/admin

e logue com as credenciais criadas no comando `createsuperuser` acima.

As ROTAS agora se dão por:

# GET:

localhost:8000/produtos/produto/{codigo} <- Codigo do produto

# POST:

localhost:8000/login

- Nesta você irá precisar resgatar o token do retorno chamado "access"
- E inserir em todas as requisiçoes no header:

### Authorization: Bearer {token}

localhost:8000/produtos/importar

- Passando corpo da requisição: arquivo: {o arquivo em si}

# PATCH:

localhost:8000/produtos/produto/{codigo}

- Nesta voce irá passar os parametros seguintes:
  titulo: string, preco: string

# 3 - REDIS

Para rodar o redis utilize na janela do terminal

```
$ cd redis
$ docker-compose up -d
$ docker exec -it redis-redis-1 redis-cli
```

Isso fará com que o redis inicie em seu sistema de forma automática.

# 4 - WORKER DA API

Esse sistema, por se tratar de um teste, resolvi ir por uma abordagem mais
simples e consisa. O worker em um ambiente de produção deveria idealmente ser
um micro servico apartado na qual utilizasse melhores praticas de autenticação
e validação das requisicoes feitas para ele.

Mas em minha visão a ideia de se fazer um worker neste teste é demonstrar a
sabedoria de empregar uma api de mensageria como o REDIS e um Listener para
efetuar transições assíncronas que resultariam em um timeout ou em um
esgotamento da API principal.

Portanto com este pensamento seguimos:

```
$ cd trabalhador

Agora utilizando workon ou o python crie seu ambiente virtual
para o pyenv virtualenvwrapper use:
$ mkvirtualenv api

ou para o python:
$ python -m venv env
$ source env/bin/activate

Após ambiente criado rode:
$ pip install -r requirements.txt

$ touch .envrc
ou
$ touch .env
Após gerado as variaveis de ambiente, voce deve inserir as seguintes variaveis

export CANAL_REDIS=""
export HOST_REDIS=""
export PORTA_REDIS=6379
export FILA_REDIS=0

export CHAVE_SISTEMA=""

export BD_NOME=
export BD_USUARIO=
export BD_SENHA=
export BD_HOST=
export BD_PORTA=

Em seguida:
$ python main.py
```

Para testar agora basta usar o seu aplicativo de requisições conforme o mostrado no passo 2.
