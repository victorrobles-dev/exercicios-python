# Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
primeiro = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
termo = primeiro
contador = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while contador <= total:
        print(f"{termo} -> ", end='')
        termo += razao
        contador += 1
    print(f"\033[32mPausa!\033[0m")
    mais = int(input("Quantos termos você quer mostra a mais? "))
print(f"Pogressão finalizada com {total} termos")