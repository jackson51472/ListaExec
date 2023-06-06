import random
def selecao(lista,rodada):
    tamanho = len(lista)
    for i in range(tamanho -1):
        iMin = i
        for j in range(i+1 , tamanho):
            rodada += 1
            if lista[j] < lista[iMin]:
                iMin = j

        aux = lista[i]
        lista[i] = lista[iMin]
        lista[iMin] = aux

    return lista,rodada

def bolha(lista, rodada):
    tamanho = len(lista)
    for i in range(tamanho-1, 0, -1):
        for j in range(i):
            rodada+=1
            if lista[j] > lista[j+1]:
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux

    return lista, rodada

rodada = 0
lista = ["Jose" , "Xavier", "Turing", "Ada", "Carlos", "Jobs"]

lista, rodada = bolha(lista, rodada)

print(rodada)
print(lista)