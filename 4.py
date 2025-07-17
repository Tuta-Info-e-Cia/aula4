#4. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input("Digite uma letra: ").strip().lower()

if len(letra) != 1 or not letra.isalpha():
    print("Entrada inválida. Digite apenas uma letra.")
elif letra in "aeiou":
    print("Vogal")
else:
    print("Consoante")
    