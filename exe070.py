# Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre: A) qual é o total gasto na compra. B) quantos produtos custam mais de R$1000. C) qual é o nome do produto mais barato.
menor = cont = qtd = total = 0
barato = ""
while True:

    print("\033[36m="*10,"LOJA SUPER BARATÃO","="*10)
    produto = str(input("\033[0mNome do produto: "))
    valor = int(input("Valor: R$"))
    cont += 1
    total += valor
    if valor > 1000:
        qtd += 1

    if cont == 1 or valor < menor:
        menor = valor
        barato = produto

    print("="*10,"LOJA SUPER BARATÃO","="*10)
    produto = str(input("Nome do produto: "))
    valor = float(input("Valor: R$"))
    total += valor
    if valor > 1000:
        qtd += 1
    
    continua = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
    if continua == "N":
        break

print(f"O total da compra foi de R$ \033[32m{total:.2f}\033[0m")
print(f"\033[32m{qtd}\033[0m Produtos custam mais de R$ 1.000,00")
print(f"O produto mais barato é o \033[32m{barato}\033[0m e custa R$ \033[32m{menor:.2f}\033[0m")
print(f"\033[32m{produto}\033[0m é o produto mais barato")
