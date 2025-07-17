
try:
    numero = int(input('Digite um número: '))
    #print('Deu Bom!!!')
    if(numero % 2 == 0):
        print('Este número é par')
    else:
        print('Este número é ímpar')
    #print('deu Ruim!!!')
except:
    print('Opção inválida digite um valor numérico....')
