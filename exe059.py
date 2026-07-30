# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:[ 1 ] somar, [ 2 ] multiplicar, [ 3 ] maior, [ 4 ] novos números, [ 5 ] sair do programa. Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep

num1 = float(input("Insira o primeiro valor: "))
num2 = float(input("Insira o segundo valor: "))

while True:
    opcao = int(input("Digite o número da opção desejada: \n[1] Somar \n[2] Multiplicar \n[3] Maior \n[4] Novos números \n[5] Sair do programa\n"))
    if opcao == 1:
        print(f"A soma entre os valores é igual a \033[32m{num1+num2:.2f}\033[0m")
    elif opcao == 2:
        print(f"A mutiplicação entre os valores é igual a \033[32m{num1*num2:.2f}\033[0m")
    elif opcao == 3:
        print(f"O maior entre os dois números é o \033[32m{max(num1,num2):.2f}\033[0m")
    elif opcao == 4:
        print(f"Insira os novos números.")
        num1 = float(input("Insira o primeiro valor: "))
        num2 = float(input("Insira o segundo valor: "))
    elif opcao == 5:
        print(f"\033[34mSaindo do programa...\033[0m")
        sleep(3)
        break
    else:
        print(f"\033[31mOpção inválida, tente novamente!\033[0m")
print(f"Programa encerrado!")