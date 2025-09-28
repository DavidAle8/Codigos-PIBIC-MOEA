import random

Lista1 = [0, 10, 9, 15, 18]
Lista2 = [6, 7, 8, 9, 10]

# S = [0, 10, 9, 15, 18]
# indiceAleatorio(S) = 10
# R = S
# R = [0, 10, 9, 15, 18]
# Quality(S) = 10
# Quality(R) = 0 (começa no 0)
# Quality(R) > Quality(S)
# se for, S_atual = R
# Se não, Tweak(R), onde R[0+1] = 10
# E assim vai. Tweak faz um breve ajuste no indice de R para ver se o proximo elemento é maior que o de S atual


def somaLista(Lista):
    acc = 0
    for elem in Lista:
        acc += pow(elem, 2)

    return acc



def indiceAleatorio(Lista):

    indice = random.randint(0, len(Lista) - 1)
    return indice



def Tweak(indice, tamanho_lista):

    if indice + 1 < tamanho_lista:
        return indice + 1
    else:
        return 0


def quality(Lista, indice):
    return Lista[indice]


# noinspection PyUnreachableCode
def Hill_Climbing(Lista):

    count = 0
    i = indiceAleatorio(Lista)  # Começa em um índice aleatório
    S_atual = quality(Lista, i)
    print(f"Valor inicial que temos: {S_atual}")

    R = Lista.copy()

    while count < len(Lista):

        if quality(R, i) > S_atual:
            S_atual = quality(R, i)
            print(f"Novo valor encontrado: {S_atual}")

        i = Tweak(i, len(Lista))  # Faço um pequeno ajuste
        count += 1

    return S_atual

print(f"Melhor valor encontrado: {Hill_Climbing(Lista1)}")