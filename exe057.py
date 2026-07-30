# Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

while True:
    sexo = str(input("Digite o seu sexo[M/F]: ")).strip()
    if sexo in "MmFf":
        print("\033[32mSexo validado!\033[0m")
        break
    else:
        print("\033[31mSexo inválido! digite novamente.\033[0m")
    