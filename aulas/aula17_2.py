# aluno = []
# aluno.append("Victor")
# aluno.append(26)
# print(aluno)
# galera = []
# galera.append(aluno[:])
# aluno[0] = "Maria"
# aluno[1] = 23
# galera.append(aluno[:])
# print(galera)

# galera = [["João", 20], ["Maria", 23], ["Victor", 26], ["Heloisa", 14]]
# print(galera[0], galera[3])

galera = []
dado = []
maior = menor = 0

for c in range(0, 3):
    dado.append(str(input("Digite o seu nome: ")))
    dado.append(int(input("Digite a sua idade: ")))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f"{p[0]} é maior de idade")
        maior += 1
    else:
        print(f"{p[0]} é menor de idade")
        menor += 1
print(f"Temos {maior} maiores de idade, e {menor} menores de idade")