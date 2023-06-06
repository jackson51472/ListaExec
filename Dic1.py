import random


def dicionarioAluno():
    dicAluno = {}
    dicAluno["nome"] = input("Nome do aluno: ")

    provas = int(input("Quantas provas esse aluno fez: "))
    media = 0


    for i in range(provas):
        dicAluno["notas"] = []
        nota = float(input(f"Nota do aluno na prova {i+1}: "))


        while nota > 10 or nota < 0:
            nota = float(input(f"NOTA INVALIDA!!!\n   Digite novamente a nota na prova {provas}: "))

        dicAluno["notas"].append(nota)
        media += nota

    dicAluno["media"] = media = media / (i + 1)
    print(media)


    return dicAluno
def exec():
    alunos = int(input("Numero de alunos: "))
    listaAluno = {}
    mediaTurma = 0
    for i in range(alunos):

        listaAluno[i] = dicionarioAluno()


        print("===" * 10)


        print(f'Nome Aluno: {listaAluno[i]["nome"]} / Media do aluno: {listaAluno[i]["media"]}')
        mediaTurma += listaAluno[i]["media"]

    print(listaAluno)

    mediaTurma = mediaTurma / alunos

    print(f"Media da turma:" , mediaTurma)



exec()