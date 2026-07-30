# Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
ano_atual = date.today().year
totmaior = 0
totmenor = 0

for pessoa in range(1, 8):
    ano_nasc = int(input("Digite o seu ano de nascimento: "))
    idade = ano_atual - ano_nasc
    if idade >= 18:
        totmaior += 1
        # print(f"Você tem \033[32m{idade} anos\033[0m, e é maior de idade")
    else:
        totmenor += 1
        # print(f"Você tem \033[31m{idade} anos\033[0m, e é menor de idade")
print(f"Ao todo tivemos \033[32m{totmaior}\033[0m pessoas maiores de idade \nE \033[32m{totmenor}\033[0m menores de idade")