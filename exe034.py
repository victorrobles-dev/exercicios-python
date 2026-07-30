salario = float(input("Digite o valor do seu salário: "))
aumento = (salario * 0.1) + salario

if salario <= 1250:
    print(f"Seu salário é R${salario:.2f} e o aumento é de R${salario * 0.3:.2f}, então o salário atual é de R${aumento:.2f}")
else:
    print(f"Seu salário é R${salario:.2f} e o aumento é de R${salario * 0.1:.2f}, então o salário atual é de R${aumento:.2f}")