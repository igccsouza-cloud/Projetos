## FINANCE ASSISTENT

- Gerenciador financeiro pessoal desenvolvido em python com foco registro e análise de transações.
- O sistema permite controlar transações de formas simples, evoluindo para um assistente financeiro inteligente com integração a APIs e modelo de linguagem.

## Funcionalidades:

- Inserção saldo:

    - Valor do depósito;
    - Fonte de origem; 
    - Data da transação;
    - Observações sobre o depósito;
    - Objetivo do depósito;

- Desconto de saldo:

    - Valor do desconto;
    - Destino do desconto; 
    - Data da transação;
    - Observações sobre o desconto;
    - Objetivo do desconto;

- Relatório de transação:

    - Através de uma integração com LLM no código, a mesma reúne informações das transações do mês atual
    e anteriores e retorna um relatório contendo de informações básicas como qual o saldo restante a insights e sugestões de economia.

## Stack:

 - Python;
 - SQL;
 - Evolution API;
 - LLM;

## Estrutura:

- Main.py (Interface principal);
- Database.py (camada de acesso ao banco de dados);
- Finance.db (banco de dados SQL gerado automaticamente);

## Como usar:

1- Clonar o repositório;
2- Executar o projeto;


## Observações:

- Projeto em desenvolvimento
- Algumas funcionalidades estão em fase inicial ou planejamento
- Integrações com APIs externas ainda não estão totalmente implementadas

## Autor

Igor Cavalcanti - www.linkedin.com/in/igorcavalcantis