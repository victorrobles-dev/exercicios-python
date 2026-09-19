# Exercício Python 067: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
while True:
    num = int(input("Digite um número para ver sua tabuada: "))
    print("~" * 30)
    if num < 0:
            break
    for n in range(1, 11):
        print(f"{num} x {n} = {num * n}")
    print("~" * 30)
print("\033[33mPrograma encerrado, volte sempre!\033[0m")
