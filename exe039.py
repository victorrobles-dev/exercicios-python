# Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date

ano_nasc = int(input("Digite seu ano de nascimento: "))
ano_atual = date.today().year
idade = ano_atual - ano_nasc

if idade < 18:
    saldo = 18 - idade
    print(f"Você atualmente tem {idade} anos\nFaltam {saldo} anos para se alistar!")
elif idade == 18:
    print(f"Você atualmente tem {idade} anos\nEstá no hora de se alistar meu chapa!")
else:
    saldo = idade - 18
    print(f"Você atualmente tem {idade} anos\n Você deveria ter se alistado a {saldo} anos")