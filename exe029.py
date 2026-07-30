velocidade_permitida = 80
velocidade_atual = int(input("Digite a velocidade em que você está: "))

if velocidade_atual > 80:
    print(f"Sua velocidade atual é {velocidade_atual} Km/h e ultrapassou o limite, você foi multado")
else:
    print(f"Sua velocidade atual é {velocidade_atual} Km/h e está dentro do limite permitido")
