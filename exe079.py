# Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente. 
lista = []
num_duplicado = []

while True:
    num = int(input("Digite um valor: "))
    lista.append(num)
    print("Valor adicionado com sucesso!")
    continua = str(input("Deseja continuar? [S/N]")).strip().upper()
    if continua == "N":
        break
    if num in lista == num:
        lista.remove(num)

print(f"Valores na lista: {lista}")