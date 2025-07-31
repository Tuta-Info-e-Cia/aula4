"""
21. Faça um Programa para um caixa eletrônico. 
O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. 
As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. 
O valor mínimo é de 10 reais e o máximo de 600 reais. 
O programa não deve se preocupar com a quantidade de notas existentes na máquina.
- Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
- Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
"""

# Programa para simular um caixa eletrônico

# Solicita o valor do saque
valor = int(input("Digite o valor do saque (entre 10 e 600 reais): "))

# Verifica se o valor está dentro do limite permitido
if valor < 10 or valor > 600:
    print("Valor inválido. O saque deve ser entre R$10 e R$600.")
else:
    print(f"Valor a sacar: R${valor}")

    # Cálculo da quantidade de notas
    notas100 = valor // 100
    valor %= 100

    notas50 = valor // 50
    valor %= 50

    notas10 = valor // 10
    valor %= 10

    notas5 = valor // 5
    valor %= 5

    notas1 = valor

    # Exibição das notas
    if notas100 > 0:
        print(f"{notas100} nota(s) de R$100")
    if notas50 > 0:
        print(f"{notas50} nota(s) de R$50")
    if notas10 > 0:
        print(f"{notas10} nota(s) de R$10")
    if notas5 > 0:
        print(f"{notas5} nota(s) de R$5")
    if notas1 > 0:
        print(f"{notas1} nota(s) de R$1")
