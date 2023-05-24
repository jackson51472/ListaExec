import random
import time

tempo_Inicio = time.time()
vet = [random.randint(0, 15000) for i in range(1500)]
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
            print(f"Chave {chave:.0f} encontrada na posição {meio:.0f} \nVezes rodada {rodadas}")
            break
        elif chave < vet[meio]:
            dir = meio - 1
        elif chave > vet[meio]:
            esq = meio + 1

def achar_Recursiva(vet, chave, esq, dir, rodada):
    rodada += 1

    meio =int((esq+dir)/2)

    if vet[meio] == chave:
         return f"Chave {chave:.0f} encontrada na posição {meio:.0f}  \nVezes rodada {rodada}"

    elif chave < vet[meio]:
        dir = meio - 1


        return achar_Recursiva(vet, chave, dir, esq, rodada)

    elif chave > vet[meio]:
        esq = meio + 1

        return achar_Recursiva(vet, chave, dir, esq, rodada)


print(f"Numero: {num:.0f}")

dir, esq = 0, len(vet)-1

rodadas = 0
achar_Repeticao(vet,num)
tempo_Fim = time.time()

print(f"{tempo_Fim - tempo_Inicio:.4f}")
