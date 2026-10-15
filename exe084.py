# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas, B) Uma listagem com as pessoas mais pesadas, C) Uma listagem com as pessoas mais leves.
temp = []
princ = []
maior  = menor = 0
while True:
    temp.append(str(input("Digite o nome: ")))
    temp.append(float(input("Digite o peso: ")))

    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]

    princ.append(temp[:])
    temp.clear()

    continua = str(input("Deseja continuar? [S/N]")).strip()
    if continua in "Nn":
        break

print(f"Dados principais: \033[36m{princ}\033[0m")
print(f"Você cadastrou {len(princ)} pessoas")
print(f"O maior peso é {maior} Kg")
print(f"O menor peso é {menor} Kg")
