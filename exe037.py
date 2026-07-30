# Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
num = int(input("Digite um número inteiro qualquer: \n"))
opcao = int(input("Qual será a base de conversão? Digite: \n 1: para binário\n 2: para octal\n 3: para hexadecimal: "))

if opcao == 1:
    print(f"O número {num} em Binário é = {bin(num)}")
elif opcao == 2:
    print(f"O número {num} em Octal é = {oct(num)}")
elif opcao == 3:
    print(f"O número {num} em Hexadecimal é = {hex(num)}")
else:
    print("Opção inválida!")