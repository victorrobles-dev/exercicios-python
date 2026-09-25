campeonato = ('Flamengo','palmeiras','CA Paranaense PR','Santos FC SP',
              'Fluminense RJ','Bahia','Cruzeiro','Atlético Mineiro MG',
              'Coritiba PR','Red Bull Bragantino SP')
print("-=-"*15)
print(f"Lista de times do Brasileirão: {campeonato}")
print("-=-"*15)
print(f"Os 5 primeiros são: {campeonato[:5]}")
print("-=-"*15)
print(f"O 4 últimos são: {campeonato[6:]}")
print("-=-"*15)
print(f"Times em ordem alfabética: {sorted(campeonato)}")
print("-=-"*15)
print(f"O Santos FC SP está na {campeonato.index("Santos FC SP")}° posição!")
