"""
    11. As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.

Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
- salários até R$ 280,00 (incluindo) : aumento de 20%
- salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
- salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
- salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
- o salário antes do reajuste;
- o percentual de aumento aplicado;
- o valor do aumento;
- o novo salário, após o aumento.

    """
    
def calcular_reajuste(salario):
    if salario <= 280.00:
        percentual = 20
    elif salario <= 700.00:
        percentual = 15
    elif salario <= 1500.00:
        percentual = 10
    else:
        percentual = 5

    aumento = salario * (percentual / 100)
    novo_salario = salario + aumento

    print(f"Salário antes do reajuste: R$ {salario:.2f}")
    print(f"Percentual de aumento aplicado: {percentual}%")
    print(f"Valor do aumento: R$ {aumento:.2f}")
    print(f"Novo salário após o aumento: R$ {novo_salario:.2f}")


# Solicita o salário ao usuário
try:
    salario_atual = float(input("Digite o salário do colaborador: R$ "))
    calcular_reajuste(salario_atual)
except ValueError:
    print("Por favor, digite um valor numérico válido.")