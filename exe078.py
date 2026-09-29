# Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
lista = []
pos_maior = []
pos_menor = []

for pos in range(0, 5):
    num = int(input("Digite um valor: "))
    lista.append(num)
for pos, valor in enumerate(lista):
    if valor == max(lista):
        pos_maior.append(pos)
    if valor == min(lista):
        pos_menor.append(pos)

print(f"Os valores inseridos na lista foram: \033[36m{lista}\033[0m")
print(f"O maior valor da lista é o \033[32m{max(lista)}\033[0m e sua posição é a {pos_maior}° e o menor valor é o \033[32m{min(lista)}\033[0m e sua posição é a {pos_menor}°")