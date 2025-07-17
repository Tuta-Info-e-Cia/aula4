#2. Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

numero = float(input("Digite um número: "))

if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")