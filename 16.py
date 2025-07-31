import math  # importa a biblioteca para usar a função sqrt

# Entrada do coeficiente A
a = float(input("Digite o valor de A: "))

# Verifica se é uma equação do 2º grau
if a == 0:
    print("A equação não é do segundo grau. Encerrando o programa.")
else:
    # Só pede B e C se A for diferente de zero
    b = float(input("Digite o valor de B: "))
    c = float(input("Digite o valor de C: "))

    delta = b**2 - 4*a*c

    if delta < 0:
        print("A equação não possui raízes reais.")
    elif delta == 0:
        x = -b / (2*a)
        print(f"A equação possui uma raiz real: x = {x}")
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"As raízes da equação são: x1 = {x1} e x2 = {x2}")