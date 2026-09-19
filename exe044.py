# Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento: à vista dinheiro/cheque: 10% de desconto, à vista no cartão: 5% de desconto, em até 2x no cartão: preço formal, 3x ou mais no cartão: 20% de juros.
valor_produto = float(input("Informe o valor das suas compras: R$\033[32m"))
pagamento = int(input("""\033[0mInforme a condição de pagamento:
    [1] À vista dinheiro/cheque: 10% de desconto
    [2] À vista no cartão: 5% de desconto
    [3] Em até 2x no cartão: preço formal
    [4] Em até 3x ou mais no cartão: 20% de juros\n"""))

if pagamento == 1:
    total = valor_produto - (valor_produto * 0.10)

elif pagamento == 2:
    total = valor_produto - (valor_produto * 0.05)

elif pagamento == 3:
    total = valor_produto
    parcela = total / 2
    print(f"Sua compra será parcelada em 2x de R$ {parcela:.2f}")

elif pagamento == 4:
    total = valor_produto + (valor_produto * 0.2)
    total_parcelas = int(input("Quantas parcelas serão? "))
    parcela = total / total_parcelas
    print(f"Sua compra será parcelada em {total_parcelas}x de R$ {parcela:.2f} COM JUROS")
else:
    total = valor_produto
    print("\033[31mOpção inválida! Tente novamente\033[0m")

print(f"Sua compra de R$ {valor_produto:.2f} vai custar R$ \033[32m{total:.2f}\033[0m no final.")
