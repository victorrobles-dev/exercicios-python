# Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
num = int(input("Digite um número: "))
contador = num
fatorial = 1
print(f"Calculando {num}! = ", end=' ')

while contador > 0:
    print(f"{contador}", end=' ')
    print(f" x " if contador > 1 else " = ", end=' ')
    fatorial *= contador
    contador -= 1
print(f"{fatorial}")