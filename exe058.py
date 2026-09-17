# Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint

ia = randint(0, 10)
print("Sou a IA-divinhação, vamos ver se você consegue adivinhar que número estou pensando...")
palpite = int(input("Digite o seu palpite: "))
qtd_tentativas = 0

while palpite != ia:
        palpite = int(input("Errou! Tente novamente: "))
        qtd_tentativas += 1
print(f"Acertou em \033[32m{qtd_tentativas} palpites\033[0m, parabéns!")
