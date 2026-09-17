n = int(input("Digite um número para calcular seu fatorial: "))
c = n
f = 1
print(f"Calculando {c}! ... ", end="\n")
while c > 0:
    print(f"{c}", end="")
    print(f" x " if c > 1 else " = ", end="")
    f *= c
    c -= 1
print(f"{f}")
    
