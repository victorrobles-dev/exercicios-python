# Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
lista = []
lista_pares = []
lista_impares = []

while True:
    num = lista.append(int(input("Digite um número: ")))
    continua = str(input("Deseja continuar? [S/N]")).strip()
    if continua in "Nn":
        break

print(f"A lista completa é: \033[36m{lista}\033[0m")
for num in lista:
    if num % 2 == 0:
        lista_pares.append(num)
    else:
        lista_impares.append(num)
print(f"A lista com números pares é: \033[32m{lista_pares}\033[0m")
print(f"A lista com números ímpares é: \033[32m{lista_impares}\033[0m")
