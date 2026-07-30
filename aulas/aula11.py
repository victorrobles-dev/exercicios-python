# Aula sobre cores no terminal em Python \033[0;31;41m
# a = 3
# b = 5
# print(f"Os valores são \033[32m{a} e \033[31m{b}")

# nome = 'Victor'
# print(f"Muito prazer em te conhecer \033[31m{nome}\033[31m!!")

cores = {
    'limpa': '\033[m',
    'azul': '\033[34m',
    'amarelo': '\033[33m',
    'pretoEbranco': '\033[7;30m'
}

print(cores)