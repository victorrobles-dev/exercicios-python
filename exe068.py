# Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
while True:
    num = int(input("Diga um valor: "))
    ia = randint(0, 11)
    total = num + ia
    print(f"Você jogou {num} e o computador {ia}. Total é = {total}")
    # jogador = str(input("Par ou Ímpar [P/I]? ")).strip().upper()[0]

    # if ia % 2 == 0:
    #     print("Par")
    # else:
    #     print("Ímpar")
    