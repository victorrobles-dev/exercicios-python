# Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações: Quantidade de notas, A maior nota, A menor nota, A média da turma, A situação (opcional).
def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita mais de uma).
    :param sit: valor opcional, indicando se deve adicionar ou não a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    r = {}
    r["total"] = len(n)
    r["maior"] = max(n)
    r["menor"] = min(n)
    r["media"] = sum(n) / len(n)
    if sit:
        if r["media"] >= 7:
            r["situação"] = "Bom"
        elif r["media"] >= 5:
            r["situação"] = "Razoável"
        else:
            r["situação"] = "Ruim"
    return r

resp = notas(5, 7, 9, sit=True)
print(resp)
help(notas)
