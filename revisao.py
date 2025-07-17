# modulo so olha pro resto da divisao para saber se o numero é par ou se é impar
#quando o resto é igual a zero significa que o número é par
#quando o resto for diferente de zero então o número é ímpar
#lembrando que resto igual a zero, ou seja em números pares, é atribuido por true no vscode em phyton /// e resto diferente de zero, ou seja números ímpares aparece como false
# simbolo de diferente é colocado desse jeito =>> !=
print(12 %4 == 0)

n = int(input('Digite um valor numérico:'))
if(n %2 == 0):
    print(f'O número, {n}, digitao é par')
else:
    print(f'O número, {n}, digitado é ímpar')
