# 
palavras = ('python','linguagem','tecnologia','programaçao',
            'framework','biblioteca','dados','aprendizado',
            'disciplina','foco')

for palavra in palavras:
    print(f"\nA palavra \033[36m{palavra.upper()}\033[0m tem as vogais", end=' ')
    for vogal in palavra:
        if vogal.lower() in "aeiou":
            print(f"\033[32m{vogal}\033[0m", end=' ')
