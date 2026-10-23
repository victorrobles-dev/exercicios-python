# Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
jogador = {}
partidas = []
time = []

while True:
    jogador.clear()
    jogador["Nome"] = str(input("Digite o nome do jogador: "))
    total = int(input(f"Quantas partidas o {jogador["Nome"]} jogou? "))
    partidas.clear()

    for c in range(0, total):
        partidas.append(int(input(f"Quantos gols ele fez em sua {c+1}° partida? ")))
    jogador["Gols"] = partidas[:]
    jogador["Total"] = sum(partidas)
    time.append(jogador.copy())

    while True:
        continua = str(input("Deseja continuar? [S/N] ")).upper()[0]
        if continua in "SN":
            break
        else:
            print("Opção inválida, digite somente S ou N")
    if continua == "N":
        break
# Validação dos dados
print("=-"*30)
print("Cód", end="")
for i in jogador.keys():
    print(f"{i:<15}", end="")
print()
print("=-"*30)
for k, v in enumerate(time):
    print(f"{k:>4} ", end="")
    for d in v.values():
        print(f"{str(d):<15}", end="")
    print()
print("=-"*30)




# for k, v in jogador.items():
#     print(f"O campo {k} tem o valor \033[32m{v}\033[0m")
# print("=-"*30)
# print(f"O jogador {jogador["Nome"]} jogou {total} partidas.")
# print("=-"*30)
# for pos, i in enumerate(partidas):
#     print(f"  => Na {pos+1}° partida, fez {i} gols.")
# print(f"Seu saldo foi de {sum(jogador["Gols"])} gols.")
