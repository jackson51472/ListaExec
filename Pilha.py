from array import array

vet = array("i", (0 for i in range(6)))
ultimo  = 0

def empilhar(vetor, cont_Ultimo,numero):
    if cont_Ultimo >= len(vetor):
        print("impossível colocar mais numeros")
        return vetor,cont_Ultimo
    else:
        vetor[cont_Ultimo] = numero

        return vetor, cont_Ultimo + 1

def desempilha(vet, ultimo):
    if ultimo == 0:
        print("Não tem o que desempilha")
        return vet,ultimo
    else:
        vet[ultimo-1] = 0
        return vet , ultimo - 1


vet,ultimo = empilhar(vet,ultimo,99)
vet,ultimo = empilhar(vet,ultimo,99)
vet,ultimo = empilhar(vet,ultimo,99)
vet,ultimo = empilhar(vet,ultimo,99)

vet,ultimo = desempilha(vet, ultimo)



print(ultimo)
print(vet)