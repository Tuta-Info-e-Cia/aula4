#1. Faça um Programa que peça dois números e imprima o maior deles.
try:
       
    n1 = int(input('Digite um número:'))
    n2 = int(input('Digite outro número:'))
    if(n1 > n2):
        print(f'O maior número é: {n1}')
    else:
        print(f'O maior número é: {n2}')
except:
    print('Opção Inválida - Digite um valor numérico...')
    
    