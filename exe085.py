# Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
lista = []

for num in range(0, 7):
    lista.append(int(input(f"Digite o primeiro número: ")))

    # if num % 2 == 0:
    #     lista.append(num)
    # else:
    #     lista.append(num)
print(f"A lista de números pares é {lista}")