# Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
qtdmulheres = 0

for p in range(1, 5):
    print(f"\033[32m------- {p}ª Pessoa --------\033[0m")
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo[M/F]: ")).strip()
    somaidade += idade

    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        qtdmulheres += 1

mediaidade = somaidade / 4
print(f"\033[34mA media de idade entre os participantes é de {mediaidade} anos!\033[0m")
print(f"O homem mais velho tem \033[32m{maioridadehomem}\033[0m anos e se chama \033[32m{nomevelho}\033[0m.")
print(f"\033[32m{qtdmulheres}\033[0m mulheres tem menos de 20 anos de idade.")
