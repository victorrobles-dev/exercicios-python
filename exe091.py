# Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter

dado = {
    "Jogador 1": randint(1, 6),
    "Jogador 2": randint(1, 6),
    "Jogador 3": randint(1, 6),
    "Jogador 4": randint(1, 6)
}
rank = {}

print("\033[36m<<< Jogadas >>>\033[0m")
for k, v in dado.items():
    print(f"{k} tirou {v} no dado.")
    sleep(1)
print("\033[36m<<< Ranking dos Jogadores >>>\033[0m")
rank = sorted(dado.items(), key=itemgetter(1), reverse=True) # Chama o método sorted e o import itemgetter para ranquear os valores na posição 1, pois os valores estão sendo tratados como uma lista
for pos, v in enumerate(rank):
    print(f"\033[32m{pos+1}° lugar:\033[0m {v[0]} com {v[1]}.")
    sleep(1)
