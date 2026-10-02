# Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre: A) Quantos números foram digitados. B) A lista de valores, ordenada de forma decrescente. C) Se o valor 5 foi digitado e está ou não na lista.
lista = []

while True:
    lista.append(int(input("Digite um valor: ")))
    lista.sort(reverse=True)
    continua = str(input("Deseja continuar? [S/N]")).strip()
    if continua in "Nn":
        break

print(f"Quantidade de valores digitados: \033[32m{len(lista)}\033[0m")
print(f"Valores na lista de forma decrescente: \033[36m{lista}\033[0m")
print("\033[32mO valor 5 está na lista\033[0m" if 5 in lista else "\033[31mO valor 5 não está na lista\033[0m")
