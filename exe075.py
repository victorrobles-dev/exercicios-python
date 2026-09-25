# Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre: A) Quantas vezes apareceu o valor 9. B) Em que posição foi digitado o primeiro valor 3. C) Quais foram os números pares.
num = (int(input("Digite o primeiro número: ")), int(input("Digite o segundo número: ")),
       int(input("Digite o terceiro número: ")), int(input("Digite o quarto número: ")))
print("~"*35)
print(f"O número 9 aparece \033[32m{num.count(9)}\033[0m vezes")
print("~"*35)
if 3 in num:
    print(f"O número 3 apareceu na \033[32m{num.index(3)+1}° posição\033[0m")
print("~"*35)
for n in num:
    if n % 2 == 0:
        print(f"{n} é um número \033[32mpar\033[0m")
    