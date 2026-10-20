# Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
from time import sleep
lista = []
jogos = []
qtd_jogos = int(input("Quantos jogos deseja fazer? "))
tot = 1

while tot <= qtd_jogos:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print(f"\033[36mSorteando {qtd_jogos} jogos...\033[0m")
for i, l in enumerate(jogos):
    print(f"\033[32m{i+1}° Jogo:\033[0m {l}")
    sleep(1)
print("\033[36mFim! boa sorte!\033[0m")