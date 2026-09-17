# Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = str(input("Digite o seu sexo: ")).strip().upper()
while sexo not in "MmFf":
    sexo = str(input("\033[31mDados inválidos\033[0m, digite o seu sexo novamente: ")).strip().upper()
print("\033[32mSexo validado!\033[0m")