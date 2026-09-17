#Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:[ 1 ] somar, [ 2 ] multiplicar, [ 3 ] maior, [ 4 ] novos números, [ 5 ] sair do programa, seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
opcao = 0

while opcao != 5:
    print("""
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair
    """)
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        print(f"A soma entre {num1} e {num2} é igual a = \033[32m{num1+num2}\033[0m")
    elif opcao == 2:
        print(f"A multiplicação entre {num1} e {num2} é igual a = \033[32m{num1*num2}\033[0m")
    elif opcao == 3:
        if num1 == num2:
            print("Não existe número maior, pois ambos são o mesmo.")
        else:
            print(f"O maior número entre {num1} e {num2} é o \033[32m{max(num1,num2)}\033[0m")
    elif opcao == 4:
        num1 = int(input("Digite o primeiro novo número: "))
        num2 = int(input("Digite o segundo novo número: "))
    elif opcao == 5:
        print("Encerrando sistema...")
        sleep(3)
        break
    else:
        print("Opção inválida, digite novamente...")
print("\033[32mSistema encerrado!\033[0m")
