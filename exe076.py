# Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
listagem = ("Lápis", 1.99,
            "Lapiseira", 3.50,
            "Caneta", 2.75,
            "Borracha", 4.00,
            "Apontador", 5.75,
            "Caderno", 15.00,
            "Dicionário", 10.00,
            "Mochila", 115.00
)
print("-"*30)
print("LISTAGEM DE PREÇOS".center(30))
print("-"*30)
print(f"""
{listagem[0]}..................R$ {listagem[1]:.2f}
{listagem[2]}..................R$ {listagem[3]:.2f}
{listagem[4]}..................R$ {listagem[5]:.2f}
{listagem[6]}..................R$ {listagem[7]:.2f}
{listagem[8]}..................R$ {listagem[9]:.2f}
{listagem[10]}.................R$ {listagem[11]:.2f}
{listagem[12]}.................R$ {listagem[13]:.2f}
{listagem[14]}.................R$ {listagem[15]:.2f}""")
print("-"*30)
