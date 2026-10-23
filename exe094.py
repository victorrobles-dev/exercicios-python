# Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas, B) A média de idade, C) Uma lista com as mulheres, D) Uma lista de pessoas com idade acima da média
dicionario = {}
lista = []
soma = media = 0
# Inserção de dados
while True:
    dicionario.clear()
    dicionario["Nome"] = str(input("Digite o nome: "))

    while True:
        dicionario["Sexo"] = str(input("Digite o sexo: [M/F] ")).upper()[0]
        if dicionario["Sexo"] in "MF":
            break
        print("Opção inválida! digite somente M ou F")
    dicionario["Idade"] = int(input("Digite a idade: "))
    soma += dicionario["Idade"]
    lista.append(dicionario.copy())
    media = soma / len(lista)

    while True:
        continua = str(input("Deseja continuar? [S/N] ")).upper()[0]
        if continua in "SN":
            break
        print("Opção inválida! digite somente S ou N")
    if continua == "N":
        break
print("=-"*30)
# Aqui começa a validação dos dados
print(f"Quantidade de pessoas cadastradas: \033[32m{len(lista)} pessoas\033[0m.")
print(f"A média de idade é: \033[32m{media:.2f} anos\033[0m.")
print("\033[34mLista de mulheres:\033[0m")
for mulher in lista:
    if mulher["Sexo"] == "F":
        print(f" => {mulher["Nome"]}")
print('=-'*30)
print("\033[35mLista de pessoas com idade acima da média:\033[0m")
for pessoa in lista:
    if pessoa["Idade"] >= media:
        print()
        for k, v in pessoa.items():
            print(f"{k}: {v}")
print("<<< Encerrado >>>")