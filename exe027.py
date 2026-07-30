#Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente. Ex: Ana Maria de Souza (primeiro = Ana; último = Souza).
n = input("Digite o seu nome e sobrenome: ").strip()
name = n.split()
print(f"Seu nome é {name[0]}")
print(f"Seu último nome é {name[len(name)-1]}")
