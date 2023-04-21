import random


def atividadesUm(tupla):

    tupla = list(tupla)

    retorno = False

    for i in range(len(tupla)):
        if tupla[0] == tupla[i]:
            retorno = True
        else:
            retorno = False


    return retorno
def inverte(tuplaUm):
    tuplaReserva = tuplaUm
    tuplaUm = list(tuplaUm)

    tuplaUm.reverse()

    tuplaUm , tuplaReserva = tuple(tuplaUm), tuple(tuplaReserva)

    return tuplaUm
def intercala(tuplaUm, tuplaDois):
    tuplaUm = list(tuplaUm)
    tuplaDois = list(tuplaDois)
    tuplaIntercalada = []

    for i in range(3):
        tuplaIntercalada.append(tuplaUm[i])
        tuplaIntercalada.append(tuplaDois[i])

    tuplaUm, tuplaDois, tuplaIntercalada = tuple(tuplaUm), tuple(tuplaDois), tuple(tuplaIntercalada)

    return tuplaIntercalada
def opera(tupla, numeroUm, numeroDois):


    if tupla[0].lower() == "soma":
        return f"Soma || {numeroUm} + {numeroDois} = {numeroUm + numeroDois}"
    elif tupla[0].lower() == "sub":
        return f"Subtração ||  {numeroUm} - {numeroDois} =  {numeroUm - numeroDois}"
    elif tupla[0] .lower() == "mult":
        return f"Multiplicação || {numeroUm} * {numeroDois} = {numeroUm * numeroDois}"
    else:
        return f"Divisão || {numeroUm} / { numeroDois} = {numeroUm / numeroDois:.2f}"
def start():

    continua = True

    while continua:

        tipo_Atividade = int(input("""1)Escreva uma função que recebe uma tupla e retorna True se o
primeiro elemento for igual ao último elemento da tupla.

==========================================================================================================================
2)Escreva uma função inverte() que recebe uma tupla de trêselementos e retorna uma nova tupla com os elementos na
ordem reversa.

==========================================================================================================================
3)Escreva a função intercala() que recebe duas tuplas de trêselementos cada e retorna uma tupla de seis elementos
intercalando as duas tuplas.

==========================================================================================================================
4)Escreva a função opera() que recebe uma tupla com umastring e dois números. Se a string for ’SOMA’, retorna a soma
dos dois números, se for ’MULT’, retorna a multiplicação, sefor ’DIV’, retorna a divisão, se for ’SUB’, retorna a subtração,
se não for nenhuma das anteriores retorna None.

==========================================================================================================================
Qual atividade você quer ver?
--> """))

        while tipo_Atividade < 1 or tipo_Atividade > 4:
            tipo_Atividade = int(input("Não tem essa atividade, digite novamente:"))


        if tipo_Atividade == 1:

            tuplaUm = []
            for i in range(5):
                tuplaUm.append(random.randint(0, 9))

            tuplaUm = tuple(tuplaUm)

            print(f"Tupla = {tuplaUm}")
            print("REPETIDOS = ",atividadesUm(tuplaUm))
            print("===" * 30)

        else:
            if tipo_Atividade == 2:

                tuplaUm = []

                for i in range(5):
                    tuplaUm.append(random.randint(0, 9))

                tuplaUm = tuple(tuplaUm)

                print("INVERTIDA:     ", inverte(tuplaUm))
                print("NÃO INVERTIDA: ", tuplaUm)

                print("===" * 30)


            else:
                if tipo_Atividade == 3:
                    tuplaUm = []
                    tuplaDois = []
                    for i in range(3):
                        tuplaUm.append(random.randint(0, 9))
                        tuplaDois.append(random.randint(0, 9))

                    tuplaUm, tuplaDois = tuple(tuplaUm), tuple(tuplaDois)

                    print("Tupla 1:", tuplaUm)
                    print("Tupla 2:", tuplaDois)
                    print("Tupla Intercalada", intercala(tuplaUm,tuplaDois))

                    print("===" * 30)

                else:
                    tuplaUm = [input("Tipo: [SOMA][SUB][MULT][DIV] ")]
                    tuplaUm = tuple(tuplaUm)
                    numeroUm = int(input("Numero 1: "))
                    numeroDois = int(input("Numero 2: "))

                    print(opera(tuplaUm,numeroUm,numeroDois))

                    print("===" * 30)
        continua = int(input("Deseja continuar? [1]SIM [2]NÃO |-->"))

        if continua > 2 or continua < 1:
            continua = int(input("Não existe essa opção, digite novamente\nDeseja continuar? [1]SIM [2]NÃO "))

        continua = True if continua == 1 else False
        
start()