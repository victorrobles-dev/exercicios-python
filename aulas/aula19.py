# pessoa = {"nome":"Victor", "idade":24, "Endereço":"Rua das Américas"}
# print(pessoa.keys())
# print(pessoa.values())
# print(pessoa.items())

estado = {}
brasil = []
for c in range(0, 3):
    estado["uf"] = str(input("Digite a unidade federativa: "))
    estado["sigla"] = str(input("Digite a sigla do estado: "))
    brasil.append(estado.copy())

for e in brasil:
    for v in e.values():
        print(v, end=" ")
    print()