# Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg)).strip()
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(f"\033[31mDigite um número inteiro válido\033[0m")
        if ok:
            break
    return valor

# Programa principal
n = leiaInt("Digite um número: ")
print(f"Você acabou de digitar o número {n}")
