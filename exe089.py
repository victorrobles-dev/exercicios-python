# Exercício Python 089: Crie um programa que leia um nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
from time import sleep
boletim = []
while True:
    nome = str(input("Digite o seu nome: "))
    nota1 = float(input("Digite a 1° nota: "))
    nota2 = float(input("Digite a 2° nota: "))
    media = (nota1 + nota2) / 2
    boletim.append([nome, [nota1,nota2], media])
    continua = str(input("Deseja continuar? [S/N]")).strip()
    if continua in "Nn":
        break

print("-=-"*15)
print(f"{"No.":<4}{"Nome":<10}{"Média":>8}")
print("-=-"*15)
for i, a in enumerate(boletim):
    print(f"{i:<4}{a[0]:<10}{a[2]:>8}")
while True:
    opcao = int(input("Mostrar as notas de qual aluno? (999 interrompe): "))
    if opcao == 999:
        print("Finalizando...")
        sleep(1)
        break
    if opcao <= len(boletim) - 1:
        print(f"Notas de \033[36m{boletim[opcao][0]}\033[0m são: {boletim[opcao][1]}")
print(f"<<< Boas férias >>>")
        