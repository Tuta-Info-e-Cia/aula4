"""
24. Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
- par ou ímpar;
- positivo ou negativo;
- inteiro ou decimal.
"""

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Qual operação deseja realizar? (+, -, *, /): ")
if operacao == '+':
    resultado = num1 + num2
elif operacao == '-':
    resultado = num1 - num2
elif operacao == '*':
    resultado = num1 * num2
elif operacao == '/':
    if num2 != 0:
        resultado = num1 / num2
    else:
        print("Erro: divisão por zero.")
        exit()
else:
    print("Operação inválida.")
    exit()
print(f"\nResultado da operação: {resultado}")
if resultado > 0:
    print("O número é positivo.")
elif resultado < 0:
    print("O número é negativo.")
else:
    print("O número é zero (neutro).")
if resultado.is_integer():
    print("O número é inteiro.")
    # Verifica se é par ou ímpar (só faz sentido para inteiros)
    if int(resultado) % 2 == 0:
        print("O número é par.")
    else:
        print("O número é ímpar.")
else:
    print("O número é decimal (não é classificado como par ou ímpar).")
    