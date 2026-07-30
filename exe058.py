# Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint

ia = randint(1, 10)
tentativas = 0

while True:
    palpite = float(input("Qual é o seu palpite: "))
    tentativas += 1
    if palpite == ia:
        print("\033[32mVocê ACERTOU!\033[0m")
        break
    elif palpite > ia:
        print(f"Um pouco menos, tente novamente!")
    elif palpite < ia:
        print(f"Um pouco mais, tente novamente!")

print(f"Quantidade de tentativas = \033[34m{tentativas}\033[0m")
