#Este arquivo é responsavel por criar uma conexão com o banco de dados, criar a tabela de transações e os comandos utilizados no main.py,
#isolando a manipulação do banco de dados em um lugar específico, separando as responsabilidades e facilitando manutenção e leitura do código.

import sqlite3
from pathlib import Path
from datetime import datetime

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

def saldo():

    conn = conectar() 
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(valor) FROM transacoes")
    resultado = cursor.fetchone()[0]
    
    conn.close()

    return resultado if resultado else 0

def buscar_transacoes():

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT valor, fonte_destino, data, objetivo, observacao FROM transacoes")

    dados = cursor.fetchall()

    conn.close()

    return dados

def buscar_transacoes_mes_atual():
    
    conn = conectar()
    cursor = conn.cursor()
    hoje = datetime.now()
    mes_atual = hoje.month
    ano_atual = hoje.year

    transacoes_mes = []

    cursor.execute("SELECT valor, fonte_destino, data, objetivo, observacao FROM transacoes")
    dados = cursor.fetchall()

    for linha in dados:

        data = linha[2]

        try:

            data_obj = datetime.strptime(data, "%d-%m-%Y")
            mes_sql = data_obj.month
            ano_sql = data_obj.year
        
            if mes_sql == mes_atual and ano_sql == ano_atual:

                transacoes_mes.append(linha)

        except ValueError:

            print(f"Data inválida no banco de dados: {data}. Ignorando essa transação.")
            continue

    conn.close()

    return transacoes_mes

def despesa_fixa(valor, destino):

    # pessoa digita o valor da conta e qual é a conta na main.py
    # valor é retornado para aqui
    # mais de uma conta pode existir e deve haver suporte para todas
    # esse desconto deve ser adicionado TODOS os meses

    valores = (valor)
    destinos = (destino)

    #tentar usar matriz ou primeiro a entrar primeiro a sair 

    hoje = datetime.now()
    dia = hoje.day

    while True:

        if dia == 1:

            conn = conectar()
            cursor = conn.cursor()

            for item in valores:

                cursor.execute("""INSERT INTO transacoes (valor, fonte_destino)
                               VALUES (?,?)""", (valores, destinos))

            conn.commit()
            conn.close()