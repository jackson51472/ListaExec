from array import array

vet = array("i", (0 for i in range(6)))

ultimo  = 0
primeiro = 0

def adicionar(vetor,cont_Ultimo, numero):
    if cont_Ultimo >= len(vetor):
        print("impossível colocar mais numeros")
        return vetor,cont_Ultimo
    else:
        vetor[cont_Ultimo] = numero

        return vetor, cont_Ultimo + 1

def remorver(vetor, cont_Primeiro, cont_Ultimo):
    if cont_Ultimo == cont_Primeiro:
        cont_Ultimo = 0
        cont_Primeiro = 0
        return vet, cont_Primeiro, cont_Ultimo
    elif vetor[cont_Primeiro] == 0:
        print("Não tem o que tirar da fila")
        return vetor, cont_Primeiro, cont_Ultimo
    elif cont_Ultimo != cont_Primeiro:
        vet[cont_Primeiro] = 0
        return vetor , cont_Primeiro + 1, cont_Ultimo




vet, ultimo = adicionar(vet,ultimo,99)
vet, ultimo = adicionar(vet,ultimo,99)
vet, ultimo = adicionar(vet,ultimo,99)
vet, ultimo = adicionar(vet,ultimo,99)
vet, ultimo = adicionar(vet,ultimo,99)
vet, ultimo = adicionar(vet,ultimo,99) #Enche o Vetor
vet, primeiro, ultimo = remorver(vet, primeiro, ultimo)
vet, primeiro, ultimo = remorver(vet, primeiro, ultimo)
vet, primeiro, ultimo = remorver(vet, primeiro, ultimo)
vet, primeiro, ultimo = remorver(vet, primeiro, ultimo)
vet, primeiro, ultimo = remorver(vet, primeiro, ultimo)
vet, primeiro, ultimo = remorver(vet, primeiro, ultimo)
vet, primeiro, ultimo = remorver(vet, primeiro, ultimo) #Reinicia o Vetor

vet, ultimo = adicionar(vet,ultimo,99)
vet, ultimo = adicionar(vet,ultimo,99)


print(ultimo)
print(primeiro)
print(vet)