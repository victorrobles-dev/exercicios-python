# Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
frase = str(input("Digite uma frase: ")).strip().upper().replace(' ','')
if frase == frase[::-1]:
    print(f"\033[36m{frase[::-1]}\033[0m, É um palíndromo")
else:
    print(f"\033[36m{frase[::-1]}\033[0m, Não é palíndromo")
