#Este arquivo é responsavel por criar uma conexão com o banco de dados, criar a tabela de transações e os comandos utilizados no main.py,
#isolando a manipulação do banco de dados em um lugar específico, separando as responsabilidades e facilitando manutenção e leitura do código.

import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "transacoes.db"

def conectar():

    return sqlite3.connect(DB_PATH)

def criar_tabela():

    conn = conectar() 
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transacoes
                   
        (
            id INTEGER  PRIMARY KEY AUTOINCREMENT,
            valor REAL,
            fonte_destino TEXT,
            data TEXT,
            objetivo TEXT,
            observacao TEXT
        )
        """)
    
    conn.commit()
    conn.close()

def inserir_transacao(valor, fonte, data, objetivo, obs):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO transacoes (valor, fonte_destino, data, objetivo, observacao)
    VALUES (?,?,?,?,?)""", (valor, fonte, data, objetivo, obs))

    conn.commit()
    conn.close()

def relatorio():

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT valor, fonte_destino, data, objetivo, observacao FROM transacoes")
    dados = cursor.fetchall()

    conn.close()

    if not dados:
        print("Nenhuma transação registrada.")
    
    else:
        for linha in dados:
            print(linha)