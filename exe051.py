primeiro = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
decimo_termo = primeiro + (10 - 1) * razao

for c in range(primeiro, decimo_termo + razao, razao):
    print(f"{c}", end=' -> ')
print("\033[32mACABOU!\033[0m")
