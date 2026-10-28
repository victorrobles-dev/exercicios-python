# Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
print("-"*30)
print("     Controle de Terrenos")
print("-"*30)

largura = float(input("Digite a largura do terreno(m): "))
comprimento = float(input("Digite o comprimento do terreno(m): "))

def area(largura, comprimento):
    print(f"A área do terreno {largura}x{comprimento} é de \033[32m{largura * comprimento:.2f} m²\033[0m")

area(largura, comprimento)
