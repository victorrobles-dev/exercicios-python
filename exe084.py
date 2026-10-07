# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas, B) Uma listagem com as pessoas mais pesadas, C) Uma listagem com as pessoas mais leves.
lista = []
aluno = []
pesado = leve = 0
while True:
    aluno.append(str(input("Digite o seu nome: ")))
    aluno.append(int(input("Digite o seu peso: ")))
    lista.append(aluno[:])
    aluno.clear()

    continua = str(input("Deseja continuar? [S/N]")).strip()
    if continua in "Nn":
        break

for p in lista:
    if p[1] > 80:
        lista.append(aluno)
    else:
        lista.append(aluno)

print(f"Quantidade de pessoas cadastradas: {lista}")
print(f"A quantidade de pessoas acima de 80kg é igual a {pesado}")
print(f"A quantidade de pessoa abaixo de 80kg é igual a {leve}")
