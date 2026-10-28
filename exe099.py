# Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep

def maior(*num):
    print(f"Analisando os valores {num}")
    print(f"{num} foram informados, {len(num)} valores ao todo")
    print(f"O maior valor informado foi {max(num)}")

maior(3,4,7)