# Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint
from time import sleep
numeros = []

def sorteia(lista):
    print("Sorteando 5 valores da lista: ", end="")
    for cont in range(0, 5):
        n = (randint(1, 10))
        lista.append(n)
        print(f"\033[36m{n}\033[0m ", end="", flush=True)
        sleep(0.5)

def somaPar(lista):
    print("\nSomando os números pares da lista...")
    sleep(3)
    soma = 0
    for num in lista:
        if num % 2 == 0:
            soma += num
    print(f"A soma de números pares é igual a: \033[32m{soma}\033[0m")

# Programa principal
sorteia(numeros)
somaPar(numeros)
