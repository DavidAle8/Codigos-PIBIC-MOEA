import random
import math
from operator import truediv


class Ponto:

    def __init__(self, vezes_dominado, pontos_dominados, elementos, rank, distancia):
        self.pontos_dominados = pontos_dominados  # Quem esse ponto i domina. Quais pontos foram dominados por ele.
        self.vezes_dominado = vezes_dominado  # Quantas vezes ele é dominado. Quantos pontos tem dominancia sobre ele.
        self.elementos = elementos
        self.rank = rank
        self.distancia = distancia

    """ Getters e Setters"""

    def get_dominados(self):
        return self.pontos_dominados

    def set_dominados(self, pontos_dominados):
        self.pontos_dominados = pontos_dominados

    def get_vezes_dominado(self):
        return self.vezes_dominado

    def set_vezes_dominado(self, vezes_dominado):
        self.vezes_dominado = vezes_dominado

    def get_elementos(self):
        return self.elementos

    def set_elementos(self, elementos):
        self.elementos = elementos

    def get_rank(self):
        return self.rank

    def set_rank(self, rank):
        self.rank = rank

    def setar_elemento(self):
        for _ in range(3):
            num_aleatorio = random.randint(0, 1)
            self.elementos.append(num_aleatorio)


def gerar_populacao(lista, ponto:Ponto):

    for _ in range(5):
        ponto.setar_elemento()
        lista.append(ponto)

    return lista

def dominancia(lista1, lista2):
    A = sum(lista1)
    B = sum(lista2)

    if A < B:
        return 1
    elif B < A:
        return -1
    else:
        return 0

def verificar_dominancia(pontos:list[Ponto], frentes):
    j = 0
    for i in range(len(pontos)):
        j += i + 1
        pontos[i].pontos_dominados = []  # Quem esse ponto i domina.
        pontos[i].vezes_dominado = 0  # Quantas vezes ele é dominado. Quantos pontos tem dominancia sobre ele.
        pontos[i].rank = 0
        pontos[i].distancia = 0

        for j in range(len(pontos)):
            if dominancia(pontos[i], pontos[j]) == 1:
                pontos[i].pontos_dominados.append(pontos[j])
                pontos[j].set_vezes_dominado(1)
                break
            else:
                pontos[j].pontos_dominados.append(pontos[i])
                pontos[i].set_vezes_dominado(1)

        if pontos[i].vezes_dominado == 0:
            pontos[i].rank = 1
            frentes[i].append(pontos[i])
    i = 1

    while frentes[i] != []:
        Q = []  # Nossas novas fronteiras
        for ponto in frentes:
            for ponto_dominado in ponto.get_dominados():
                ponto_dominado.set_ponto_dominado(ponto_dominado.get_rank() - 1)

                if ponto_dominado.get_rank() == 0:
                    ponto_dominado.set_rank(i + 1)
                    Q.append(ponto_dominado)
        frentes.append(Q)
        i += 1
    return frentes




# lista = [A, B, C, D, E, F]
# frente1 = [A]
# frente2 = [B, C]
# frente3 = [D, E, F]

def crowding_distance(pontos:list[Ponto], frente, n):
    T = verificar_dominancia(pontos, frente)[0]
    l = len(T)
    T[0].distancia = math.inf
    T[n].distancia = math.inf
    # m =
    # for p






