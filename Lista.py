import random


def exec(continua):
    while continua:
        exercicio = int(input("""
1)Faça uma função que dada uma lista com 5 notas, retorne a
média das notas.
==============================================================
2)Faça uma função que, dados dois inteiros x e y, retorna uma
lista com todos os valores entre x e y (inclusive), funcionando
tanto para x <= y como para x > y.
==============================================================
3)Faça uma função que dadas duas listas de três elementos
com números inteiros, retorna uma lista onde cada elemento
é a soma dos elementos de mesma posição nas duas
primeiras listas.  
    
QUAL EXERCÍCIO VOCÊ QUER VER?
==>    
    """))
        while exercicio > 3 or exercicio < 1:
            exercicio = int(input("Esse exercício não existe, digite novamente o número do ecercício:"))

        media() if exercicio == 1 else intervaloXY() if exercicio == 2 else somaLista()

        continua = int(input("Deseja continuar? [1]SIM [2]NÃO |-->"))

        if continua > 2 or continua < 1:
            continua = int(input("Não existe essa opção, digite novamente\nDeseja continuar? [1]SIM [2]NÃO "))

        continua = True if continua == 1 else False
def media():
    listaNotas = []
    nota = 0
    for y in range(5):
        listaNotas.append(random.randint(0 , 10))
        nota += listaNotas[y]

    print("Lista de Notas:",listaNotas)
    print("Media = ", nota / (y+1))
def intervaloXY():

    numX = int(input("Digite X: "))
    numY = int(input("Digite Y: "))
    listaIntervalo = []

    if numX > numY:
        for i in range(1 + (numX - numY)):
            listaIntervalo.append(numX - i)

    else:
        if numX <= numY:
            for i in range(1 + (numY - numX)):
                listaIntervalo.append(i + numX)
    print(listaIntervalo)
def somaLista():
    tamanhoLista = int(input("Qual vai ser o tamanho das 2 lista: "))
    listaUm = [random.randint(0,10)for i in range(tamanhoLista)]
    listaDois = [random.randint(0,10)for i in range(tamanhoLista)]

    novaLista = []
    for i in range(int((len(listaUm) + len(listaDois)) / 2)):
        novaLista.append(listaUm[i] + listaDois[i])

    print("Lista 1:      ",listaUm)
    print("Lista 2:      ",listaDois)
    print("Lista somada: ",novaLista)

exec(True)