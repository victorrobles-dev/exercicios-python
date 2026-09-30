# Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente. 
lista = []

while True:
    num = int(input("Digite um valor: "))
    if num not in lista:
        lista.append(num)
        lista.sort()
        print("Valor adicionado com sucesso!")
    else:
        print("Valor duplicado, não vou adicionar!")

    continua = str(input("Deseja continuar? [S/N]")).strip()
    if continua in "Nn":
        break

print("\033[32mSistema encerrado!\033[0m")
print(f"Os valores na lista são: \033[36m{lista}\033[0m")
