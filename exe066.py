# Exercício Python 066: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
soma = qtd = 0

while True:
    num = int(input("Digite um número: "))
    if num == 999:
        break
    soma += num
    qtd += 1

print(f"\033[32m{qtd}\033[0m Números foram digitados e \033[32m{soma}\033[0m é a soma total.")
