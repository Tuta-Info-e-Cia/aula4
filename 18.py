# 18. Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.


from datetime import datetime

data_input = input("Digite uma data no formato dd/mm/aaaa: ")

try:
    data_valida = datetime.strptime(data_input, "%d/%m/%Y")
    print("A data é válida.")
except ValueError:
    print("A data é inválida.")
    