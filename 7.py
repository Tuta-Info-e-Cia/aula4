#7. Faça um Programa que leia três números e mostre o maior e o menor deles.


n1 = float(input('Digite o primeiro número:'))
n2 = float(input('Digite o segundo número:'))
n3 = float(input('Digite o terceiro número:'))
maior = max(n1, n2, n3)
menor = min(n1, n2, n3)

# Exibir os resultados
print("O maior número é:", maior)
print("O menor número é:", menor)

