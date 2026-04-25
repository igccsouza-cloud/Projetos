## CALCULADORA DE INVESTIMENTOS

Calculadora de investimentos com juros compostos com interface interativa utilizando o framework kivy.

## Funcionalidades:

- Inserção de:

    - Valor do aporte mensal;
    - Taxa de juros (%);
    - Tempo de investimento (meses);
- Cálculo automático de:

    - Total investido;
    - Valor acumulado;
    - Rendimento total;
    - Rendimento mensal estimado;
- Acúmulo de múltiplas simulações;
- Tela de resumo com total consolidado;
- Interface gráfica simples e interativa;

## Stack:

 - Python;
 - Kivy;

## Estrutura:

- Interface:

    - Tela de inserção:

        - Entrada de dados;
        - Botões:
            - Calcular (realiza o cálculo);
            - Continuar(limpa os campos para outros valores para serem somados à operação anterior);
            - Sair(conclui e vai para o resumo);
            - Fechar(fecha o app);
    - Tela de resultado:

        - Exibe o total acumulado de todas as operações realizadas
- Fórmula:
    O cálculo do investimento é baseado em juros compostos com aportes mensais:

    Investimento = Aporte * (1 + juros) * (((1 + juros)^tempo - 1) / juros)

    Onde:

        Aporte = valor mensal investido
        Juros = taxa mensal (em decimal)
        Tempo = número de meses

## Como usar:

1- Instale o Kivy;
2- Execute o script

## Observações:

Os valores devem ser inseridos corretamente (sem texto ou símbolos)
A taxa de juros deve ser informada em porcentagem (ex: 5 para 5%)
O app não possui tratamento de erros (entradas inválidas podem quebrar a execução)

## Autor

Igor Cavalcanti - www.linkedin.com/in/igorcavalcantis