"""
20. Faça um Programa para leitura de três notas parciais de um aluno. 
O programa deve calcular a média alcançada por aluno e presentar:
- A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
- A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
- A mensagem "Aprovado com Distinção", se a média for igual a 10.
"""

# Programa para cálculo de média de três notas

# Entrada das três notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Cálculo da média
media = (nota1 + nota2 + nota3) / 3

# Exibição da média com duas casas decimais
print(f"Média do aluno: {media:.2f}")

# Verificação da situação do aluno
if media == 10:
    print("Aprovado com Distinção")
elif media >= 7:
    print("Aprovado")
else:
    print("Reprovado")