import random

vet = [random.randint(0, 15000) for i in range(2000)]
num = random.choice(vet)
vet = sorted(vet)

def achar_Repeticao(vet, chave):
    esq = 0
    dir = len(vet)-1
    rodadas = 0

    while esq<=dir:
        rodadas += 1
        meio =int((esq+dir)/2)
        if chave == vet[meio]:
            print(f"Chave {chave:.0f} encontrada na posição {meio:.0f} \n Vezes rodada {rodada}")
            break
        elif chave < vet[meio]:
            dir = meio - 1
        elif chave > vet[meio]:
            esq = meio + 1

def achar_Recursiva(vet, chave, esq, dir, rodada):
    rodada += 1

    meio =int((esq+dir)/2)

    if vet[meio] == chave:
         return f"Chave {chave:.0f} encontrada na posição {meio:.0f}  \n Vezes rodada {rodada}"

    elif chave < vet[meio]:
        dir = meio - 1
        print(vet[meio])

        return achar_Recursiva(vet, chave, dir, esq, rodada)

    elif chave > vet[meio]:
        esq = meio + 1
        print(vet[meio])
        return achar_Recursiva(vet, chave, dir, esq, rodada)


print(f"Numero: {num:.0f}")

dire, esq = 0, len(vet)-1
rodadas = 0
print(achar_Recursiva(vet, num, dire, esq, rodadas))

