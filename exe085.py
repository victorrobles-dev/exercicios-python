# Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
lista = [[], []]
valor = 0

for c in range(1, 8):
    valor = int(input(f"Digite o {c}° valor: "))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)  

print(f"A lista completa é: \033[32m{lista}\033[0m")
print('-=-'*20)
lista[0].sort()
print(f"Lista de números pares: {lista[0]}")
lista[1].sort()
print(f"Lista de números ímpares: {lista[1]}")