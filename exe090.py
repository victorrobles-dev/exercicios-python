# Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
situacao = {}

nome = str(input("Digite o seu nome: "))
media = float(input("Digite a sua média: "))
if media > 5:
    situacao.copy("Aprovado!")
else:
    print("Reprovado!")

print()