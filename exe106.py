# 
from time import sleep

c = (
    "\033[m" ,          # 0 - sem cores
    "\033[30m",         # 1 - vermelho
    "\033[0;30;42m",    # 2 - verde
    "\033[0;30;43m",    # 3 - amarelo
    "\033[0;30;44m",    # 4 - azul
    "\033[0;30;45m",    # 5 - roxo
    "\033[7;30m"        # 6 - branco
)

def ajuda(com):
    help(com)

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print("~" * tam)
    print(f" {msg}")
    print("~" * tam)

# Programa principalcls
comando = ""
while True:
    titulo("Sistema de Ajuda PyHelp")
    comando = str(input("Digite a função ou biblioteca > ")).strip()
    if comando.upper() == "FIM":
        break
    else:
        ajuda(comando)
titulo("Até Logo!", 1)
