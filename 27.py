"""
27. Uma fruteira está vendendo frutas com a seguinte tabela de preços:

Até 5 Kg:
- Morango R$ 2,50 por Kg 
- Maçã R$ 1,80 por Kg

Acima de 5 Kg:
- Morango R$ 2,20 por Kg

- Maçã R$ 1,50 por Kg

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, 
receberá ainda um desconto de 10% sobre este total. 
Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

"""

kg_morango = float(input("Quantidade de morangos (Kg): "))
kg_maca = float(input("Quantidade de maçãs (Kg): "))

if kg_morango <= 5:
    preco_morango = 2.50
else:
    preco_morango = 2.20

if kg_maca <= 5:
    preco_maca = 1.80
else:
    preco_maca = 1.50

total_morango = kg_morango * preco_morango
total_maca = kg_maca * preco_maca
peso_total = kg_morango + kg_maca
valor_total = total_morango + total_maca

if peso_total > 8 or valor_total > 25:
    desconto = valor_total * 0.10
    valor_total -= desconto

print(f"\nValor a ser pago: R$ {valor_total:.2f}")

