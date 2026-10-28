# Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
def escreva(mensagem):
    tam = len(mensagem) + 4
    print("~" * tam)
    print(f"  {mensagem}")
    print("~" * tam)

escreva("CeV")
escreva("Olá, mundo!")
escreva("Eu estou aprendendo python!")
