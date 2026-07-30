# Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
house = float(input("Digite o valor de venda da casa: "))
salary = float(input("Digite o seu salário em R$: "))
years = int(input("Digite em quantos anos deseja pagar a casa: "))
prestacao = house / (years * 12) 
minimo = salary * 0.30

print(f"Para pagar uma casa de R${house:.2f} As prestações serão de R${prestacao:.2f}")

if prestacao <= minimo:
    print(f"O empréstimo \033[1;32mFOI CONCEDIDO \033[1;32m")
else:
    print(f"O empréstimo \033[1;31mNÃO FOI CONCEDIDO \033[1;31m")
