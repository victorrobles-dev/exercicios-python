# Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep

itens = ("Pedra", "Papel", "Tesoura")
computador = randint(0, 2)
jogador = int(input("""Escolha sua opção: 
    [0] Pedra
    [1] Papel
    [2] Tesoura\n"""))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")

print("-=-" * 10)
print(f"O computador jogou {itens[computador]}")
print(f"O jogador jogou {itens[jogador]}")
print("-=-" * 10)

if computador == 0:
    if jogador == 0:
        print("Empate!")
    elif jogador == 1:
        print("\033[32m Jogador Venceu!\033[0m")
    elif jogador == 2:
        print("\033[31m Jogador Perdeu!\033[0m")
    else:
        print("Jogada inválida")

elif computador == 1:
    if jogador == 0:
        print("\033[31m Jogador Perdeu!\033[0m")
    elif jogador == 1:
        print("Empate!")
    elif jogador == 2:
        print("\033[32m Jogador Venceu!\033[0m")
    else:
        print("Jogada inválida")
elif computador == 2:
    if jogador == 0:
        print("\033[32m Jogador Venceu!\033[0m")
    elif jogador == 1:
        print("\033[31m Jogador Perdeu!\033[0m")
    elif jogador == 2:
        print("Empate!")
    else:
        print("Jogada inválida")
else:
    print("Opção inválida, jogue novamente!")


