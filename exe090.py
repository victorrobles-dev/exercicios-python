# Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
dicionario = {}

dicionario["Nome"]= str(input("Digite o seu nome: "))
dicionario["Media"] = float(input(f"Média de {dicionario["Nome"]}: "))

if dicionario["Media"] >= 7:
    dicionario["Situacao"] = "Aprovado"
elif 5 <= dicionario["Media"] < 7:
    dicionario["Media"] = "Recuperação"
else:
    dicionario["Situacao"] = "Reprovado"

print("=-"*15)
for k, v in dicionario.items():
    print(f"{k} é igual a: {v}")
