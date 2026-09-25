# Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint
tupla = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print(f"Os valores sorteados foram: ", end=" ")

for n in tupla:
    print(f"\033[32m{n}\033[0m", end=" ")

print(f"\nO maior número da tupla é o \033[32m{max(tupla)}\033[0m")
print(f"O menor número da tupla é o \033[32m{min(tupla)}\033[0m")
