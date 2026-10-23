# Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
jogador = {}
partidas = []

jogador["Nome"] = str(input("Digite o nome do jogador: "))
total = int(input(f"Quantas partidas o {jogador["Nome"]} jogou? "))

for c in range(0, total):
    partidas.append(int(input(f"Quantos gols ele fez em sua {c+1}° partida? ")))
jogador["Gols"] = partidas[:]
jogador["Total"] = sum(partidas)
print("=-"*30)
print(jogador)
print("=-"*30)
for k, v in jogador.items():
    print(f"O campo {k} tem o valor \033[32m{v}\033[0m")
print("=-"*30)
print(f"O jogador {jogador["Nome"]} jogou {total} partidas.")
print("=-"*30)
for pos, i in enumerate(partidas):
    print(f"  => Na {pos+1}° partida, fez {i} gols.")
print(f"Seu saldo foi de {sum(jogador["Gols"])} gols.")
