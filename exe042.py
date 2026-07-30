# Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado: EQUILÁTERO: todos os lados iguais, ISÓSCELES: dois lados iguais, um diferente, ESCALENO: todos os lados diferentes
lado1 = int(input("Primeiro lado: "))
lado2 = int(input("Segundo lado: "))
lado3 = int(input("Terceiro lado: "))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print("Esses segmentos podem formar um triângulo!")
    if lado1 == lado2 == lado3:
        print("Triângulo EQUILÁTERO!")
    elif lado1 != lado2 != lado3 != lado1:
        print("Triângulo ESCALENO!")
    else:
        print("Triângulo ISÓSCELES!")
else:
    print("Esses segmentos não podem formar um triângulo!")