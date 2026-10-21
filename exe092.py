# Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import datetime
dados = {}

dados["Nome"] = str(input("Digite o seu nome: "))
ano_nasc = int(input("Digite o ano de nascimento: "))
dados["Idade"] = datetime.now().year - ano_nasc
dados["CTPS"] = int(input("Digite o N° da CLT: (0 se não tem) "))


if dados["CTPS"] != 0:
    dados["Contratação"] = int(input("Ano de contratação: "))
    dados["Salário"] = float(input("Salário: \033[32mR$\033[0m"))
    dados["Aposentadoria"] = dados["Contratação"] + 35

for k, v in dados.items():
    print(f"\033[32m{k}\033[0m tem o valor: \033[36m{v}\033[0m")
