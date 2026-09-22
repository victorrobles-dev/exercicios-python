# Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre: A) quantas pessoas tem mais de 18 anos. B) quantos homens foram cadastrados. C) quantas mulheres tem menos de 20 anos.
p = m = h = 0

while True:
    print("="*30)
    print("CADASTRO DE USUÁRIOS".center(30))
    print("="*30)
    idade = int(input("Digite sua idade: "))
    if idade > 18:
        p += 1
    sexo = str(input("Digite o seu sexo: [M/F] ")).strip().upper()[0]
    if sexo == "M":
        h += 1
    if sexo == "F" and idade < 20:
        m += 1

    continua = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
    if continua == "N":
        break

print(f"\033[32m{p}\033[0m Pessoas cadastradas maiores de 18 anos")
print(f"\033[32m{h}\033[0m Homens foram cadastrados no sistema")
print(f"\033[32m{m}\033[0m Mulheres cadastradas menores de 20 anos")
