# Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
lista = []

for c in range(0, 5):
    valor = int(input("Digite o primeiro valor: "))
    if c  == 0 or valor > lista[-1]:
        lista.append(valor)
        print("Adicionado ao final da lista!")
    else:
        pos = 0 
        while pos < len(lista):
            if valor <= lista[pos]:
                lista.insert(pos, valor)
                print(f"Adicionado na posição {pos} da lista!")
                break
            pos += 1

print(f"Lista ordenada: {lista}")