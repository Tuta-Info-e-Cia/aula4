dinheiro = False
senha = False


if dinheiro == True and senha == True:
    print('Sacar')
elif dinheiro == True and senha == False:
    print('Senha Inválida!')
elif dinheiro == False and senha == True:
    print('Saldo Insufiente!')
elif dinheiro == False and senha == False:
    print('Saldo Insuficiente e Senha Inválida!')
    
    