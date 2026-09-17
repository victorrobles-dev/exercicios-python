# Exercício Python 064: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
num = cont = soma = 0
num = int(input("Digite um valor, (999 para encerrar): "))
while num != 999:
    soma += num
    cont += 1
    num = int(input("Digite um valor, (999 para encerrar): "))
print(f"Você digitou \033[32m{cont}\033[0m números, e a soma é igual a \033[32m{soma}\033[0m")