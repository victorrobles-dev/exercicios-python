#Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
resp = "S"
soma = quant = media = maior = menor = 0
while resp in "Ss":
    num = int(input("Digite um número: "))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input("Deseja continuar? \033[35m[S/N]\033[0m")).lower().strip()[0]
media  = soma / num   
print(f"Acabou! quantidade de números digitados: \033[32m{num}\033[0m")
print(f"E a média foi de: \033[32m{media:.2f}\033[0m")
print(f"O maior valor foi {maior} e o menor foi {menor}")
