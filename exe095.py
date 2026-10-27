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
print("Cód ", end="")
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
while True:
    consulta = int(input("Qual jogador deseja consultar? [999] para encerrar: "))
    if consulta == 999:
        break
    if consulta >= len(time):
        print(f"Erro! não existe jogador com código {consulta}")
    else:
        print(f" -> Levantamento do jogador \033[36m{time[consulta]["Nome"]}\033[0m: ")
        print("-"*30)
        for i, g in enumerate(time[consulta]["Gols"]):
            print(f"    No {i+1}° jogo fez \033[32m{g}\033[0m gols!")
    print("-"*30)
print("Sistema encerrado")