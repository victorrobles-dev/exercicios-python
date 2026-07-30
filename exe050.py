# # Exercício Python 050: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
soma = 0
contador = 0

for n in range(1, 7):
    num = int(input(f"Digite o {n}° valor: "))
    if num % 2 == 0:
        soma += num
        contador += 1
print(f"Você informou \033[32m{contador}\033[0m número(s) pares e a soma foi \033[32m{soma}\033[0m")
