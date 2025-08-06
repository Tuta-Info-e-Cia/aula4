"""
26. Um posto está vendendo combustíveis com a seguinte tabela de descontos: 

Álcool:
- até 20 litros, desconto de 3% por litro
- acima de 20 litros, desconto de 5% por litro 

Gasolina:
- até 20 litros, desconto de 4% por litro
- acima de 20 litros, desconto de 6% por litro 

Escreva um algoritmo que leia o número de litros vendidos, 
o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), 
calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

"""

preco_alcool = 1.90
preco_gasolina = 2.50

litros = float(input("Quantos litros foram vendidos? "))
tipo = input("Tipo de combustível (A - Álcool, G - Gasolina): ").strip().upper()

desconto_por_litro = 0
preco_total = 0

if tipo == 'A':
    if litros <= 20:
        desconto_por_litro = 0.03  # 3%
    else:
        desconto_por_litro = 0.05  # 5%
    preco_bruto = litros * preco_alcool
    preco_total = preco_bruto - (preco_bruto * desconto_por_litro)

elif tipo == 'G':
    if litros <= 20:
        desconto_por_litro = 0.04  # 4%
    else:
        desconto_por_litro = 0.06  # 6%
    preco_bruto = litros * preco_gasolina
    preco_total = preco_bruto - (preco_bruto * desconto_por_litro)

else:
    print("Tipo de combustível inválido.")
    exit()

print(f"\nValor a ser pago: R$ {preco_total:.2f}")


