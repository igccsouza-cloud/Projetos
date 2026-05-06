#Este arquivo é o ponto de entrada do programa, onde o usuário escolhe o comando a ser executado (adicionar, descontar ou gerar relatório),
#cujas funções de manipulação de dados são importadas do arquivo database.py, mantendo a lógica de negócios separada da manipulação do banco de dados.

from database import inserir_transacao, criar_tabela, saldo, buscar_transacoes,buscar_transacoes_mes_atual, despesa_fixa

criar_tabela()

def salvar_transacao(valor, fonte, data, objetivo, obs):

    inserir_transacao(valor, fonte, data, objetivo, obs)

def add():

    valor = float(input("Digite o valor: "))
    fonte = str(input("Digite a fonte: "))
    data = str(input("Digite a data da transação (formato: DD-MM-YYYY): "))
    objetivo = str(input("Digite o objetivo: "))
    obs = str(input("Observação: "))

    salvar_transacao(valor, fonte, data, objetivo, obs)

    print("Valor adicionado com sucesso!")

def descont():

    valor = -float(input("Digite o preço: "))
    fonte = str(input("Digite o destino: "))
    data = str(input("Digite o data da transação (formato: DD-MM-YYYY): "))
    obs = str(input("Observação: "))
    objetivo = str(input("Digite o objetivo: "))

    salvar_transacao(valor, fonte, data, objetivo, obs)

    print("Valor descontado com sucesso!")

def report():

    print("\nRelatório de transações: \n")
    
    dados = buscar_transacoes()

    if not dados:

        print("Nenhuma transação registrada")
    
    else:

        for valor, fonte_destino, data, objetivo, observacao in dados:

            tipo = "Entrada" if valor > 0 else "Saída"

            print(f"""
                  
                  Tipo: {tipo}
                  Valor: {valor:.2f}
                  Fonte/Destino: {fonte_destino}
                  Data: {data}
                  Objetivo: {objetivo}
                  Observação: {observacao}
                  ------------------------
                  """)
            
def report_mes_atual():

    print("\nRelatório de transações do mês atual: \n")
    
    dados = buscar_transacoes_mes_atual()

    if not dados:

        print("Nenhuma transação registrada para o mês atual.")
    
    else:

        for valor, fonte_destino, data, objetivo, observacao in dados:

            tipo = "Entrada" if valor > 0 else "Saída"

            print(f"""
                  
                  Tipo: {tipo}
                  Valor: {valor:.2f}
                  Fonte/Destino: {fonte_destino}
                  Data: {data}
                  Objetivo: {objetivo}
                  Observação: {observacao}
                  ------------------------
                  """)

def saldo():

    print(f"Saldo atual: R${saldo():.2f}")

def conta_add():

    destino = str(input("Informe o nome da conta fixa"))
    valor = float(input("Digite o valor da conta"))

    despesa_fixa(valor, destino)

cmd = input("Digite o comando (add/desconto/relatório/saldo): ").lower()

print()

if cmd == "add":

    try:
        add()

    except ValueError:
        print("Valor inválido. Digite um número.")

    except Exception as e:
        print(f"Erro inesperado: {e}")
        
if cmd == "saldo":

    try:
        saldo()

    except ValueError:
        print("Valor inválido. Digite um número.")

    except Exception as e:
        print(f"Erro inesperado: {e}")
        

elif cmd == "desconto":

    try:
        descont()

    except ValueError:
        print("Valor inválido. Digite um número.")

    except Exception as e:
        print(f"Erro inesperado: {e}")
        
elif cmd == "Relatório".lower():

    try:
        report()
        
    except ValueError:
        print("Valor inválido. Digite um número.")

    except Exception as e:
        print(f"Erro inesperado: {e}")

elif cmd == "Relatório Mensal".lower():

    try:
        report_mes_atual()
        
    except ValueError:
        print("Valor inválido. Digite um número.")

    except Exception as e:
        print(f"Erro inesperado: {e}")
        
print()
