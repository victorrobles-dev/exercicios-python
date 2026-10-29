def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f"{c} ", end="")
        c += p
    print("Fim")

def somar(a=0, b=0, c=0): # <- parâmetros opcionais
    s = a + b + c
    print(f"A soma é: {s}")

somar(1,2)

def subtrai(a, b, c):
    s = a + b + c
    return s

r1 = subtrai(5,2,1)
r2 = subtrai(10,5,1)
r3 = subtrai(7,4,3)
print(f"Os resultados são {r1} {r2} e {r3}")