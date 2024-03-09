import csv
import psycopg2
from psycopg2 import sql
from os import getenv

def efetua_insercao(caminho_arquivo: str):
    '''
    A ideia é nao ter uma conexão persistente,
    O ideal em um ambiente de produção seria persistir, mas como é um teste
    não o farei aqui, diferente por ex do Redis.
    '''
    conexao = psycopg2.connect(
         dbname="produtos_db",
        user="produtos_user",
        password="admin_produtos",
        host="localhost",
        port=5432
    )

    conexao.autocommit = False
    cursor = conexao.cursor()
    try:
        with open(caminho_arquivo, 'r', newline='') as arquivo:
            leitor = csv.reader(arquivo)
            next(leitor)

            for row in leitor:
                cursor.execute(
                    sql.SQL("INSERT INTO produto_produto (codigo, titulo, preco) VALUES (%s, %s, %s)"),
                    row
                )
        conexao.commit()

    except Exception as e:
        conexao.rollback()
        print("Erro durante a inserção:", e)

    finally:
        cursor.close()
        conexao.close()
