# Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
primeiro = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
termo = primeiro
contador = 1

while contador <= 10:
    print(f"{termo} -> ", end='')
    termo += razao
    contador += 1
print(f"\033[32mFim!\033[0m")
