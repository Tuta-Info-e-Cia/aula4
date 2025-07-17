#6. Faça um Programa que leia três números e mostre o maior deles.


num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Verifica o maior número
maior = max(num1, num2, num3)

# Exibe o resultado
print("O maior número é:", maior)
