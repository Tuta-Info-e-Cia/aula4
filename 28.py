"""
28. O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. 

Confira:

Até 5 Kg:
- File Duplo R$ 4,90 por Kg
- Alcatra R$ 5,90 por Kg
- Picanha R$ 6,90 por Kg

Acima de 5 Kg:
- File Duplo R$ 5,80 por Kg
- Alcatra R$ 6,80 por Kg
- Picanha R$ 7,80 por Kg

Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, 
porém não há limites para a quantidade de carne por cliente. 
Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. 
Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, 
contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.
"""

print("Tipos de carne disponíveis:")
print("1 - Filé Duplo")
print("2 - Alcatra")
print("3 - Picanha")
tipo = input("Escolha o tipo de carne (1/2/3): ").strip()
kg = float(input("Quantidade de carne (Kg): "))
pagamento_cartao = input("Pagamento com Cartão Tabajara? (s/n): ").strip().lower()
if tipo == '1':
    nome_carne = "Filé Duplo"
    preco = 4.90 if kg <= 5 else 5.80
elif tipo == '2':
    nome_carne = "Alcatra"
    preco = 5.90 if kg <= 5 else 6.80
elif tipo == '3':
    nome_carne = "Picanha"
    preco = 6.90 if kg <= 5 else 7.80
else:
    print("Tipo de carne inválido.")
    exit()
preco_total = kg * preco
if pagamento_cartao == 's':
    tipo_pagamento = "Cartão Tabajara"
    desconto = preco_total * 0.05
else:
    tipo_pagamento = "Outro"
    desconto = 0.0

valor_final = preco_total - desconto
print("\n--- CUPOM FISCAL ---")
print(f"Tipo de carne: {nome_carne}")
print(f"Quantidade: {kg:.2f} Kg")
print(f"Preço total: R$ {preco_total:.2f}")
print(f"Tipo de pagamento: {tipo_pagamento}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Valor a pagar: R$ {valor_final:.2f}")
