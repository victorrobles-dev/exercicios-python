lado1 = int(input("Primeiro lado: "))
lado2 = int(input("Segundo lado: "))
lado3 = int(input("Terceiro lado: "))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print("Esses segmentos podem formar um triângulo!")
else:
    print("Esses segmentos não podem formar um triângulo!")