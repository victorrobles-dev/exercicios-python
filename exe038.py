# Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

if num1 > num2:
    print(f"O primeiro número é o maior: {num1}")
elif num1 < num2:
    print(f"O segundo número é o maior: {num2}")
else:
    print(f"Não existe valor maior, os dois são iguais!")
