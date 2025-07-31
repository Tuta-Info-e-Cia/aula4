"""
15. Faça um Programa que peça os 3 lados de um triângulo.
 O programa deverá informar se os valores podem ser um triângulo. 
 Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno. Dicas:
- Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
- Triângulo Equilátero: três lados iguais;
- Triângulo Isósceles: quaisquer dois lados iguais;
- Triângulo Escaleno: três lados diferentes;
"""

lado1 = float(input("Digite a medida do primeiro lado do triângulo: "))
lado2 = float(input("Digite a medida do segundo lado do triângulo: "))
lado3 = float(input("Digite a medida do terceiro lado do triângulo: "))

if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    print("\nOs lados formam um triângulo!")

    if lado1 == lado2 == lado3:
        print('É um tringulo Equilátero!')
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print('É um triangulo Isósceles!')
    else:
        print('É um triangulo Escaleno!')

else:
    print("\nOs valores informados **não** formam um triângulo.")

