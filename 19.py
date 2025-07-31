"""
19. Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
 Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
- 326 = 3 centenas, 2 dezenas e 6 unidades
- 12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
"""


# Função para formatar a saída com plural e pontuação correta
def formatar_numero(numero):
    if not (0 <= numero < 1000):
        return "Número inválido. Digite um número entre 0 e 999."

    centenas = numero // 100
    dezenas = (numero % 100) // 10
    unidades = numero % 10

    partes = []

    # Adiciona a parte das centenas, se houver
    if centenas > 0:
        if centenas == 1:
            partes.append("1 centena")
        else:
            partes.append(f"{centenas} centenas")

    # Adiciona a parte das dezenas, se houver
    if dezenas > 0:
        if dezenas == 1:
            partes.append("1 dezena")
        else:
            partes.append(f"{dezenas} dezenas")

    # Adiciona a parte das unidades, se houver
    if unidades > 0:
        if unidades == 1:
            partes.append("1 unidade")
        else:
            partes.append(f"{unidades} unidades")

    # Se o número for 0
    if numero == 0:
        return "0 unidade"

    # Formata com vírgula e "e"
    if len(partes) == 1:
        return partes[0]
    elif len(partes) == 2:
        return f"{partes[0]} e {partes[1]}"
    else:
        return f"{partes[0]}, {partes[1]} e {partes[2]}"

# Programa principal
numero = int(input("Digite um número inteiro menor que 1000: "))
print(formatar_numero(numero))