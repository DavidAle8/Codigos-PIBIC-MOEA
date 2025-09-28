import random
from numpy import number
class pontos:

    def __init__(self, elementos, marcado):
        self.elementos = elementos
        self.marcado = marcado

    def setar_ponto(self):

        for num_aleatorio in range(3):
            num_aleatorio = random.randint(0, 1)
            self.elementos.append(num_aleatorio)

        self.marcado = False


def gerar_lista(lista, ponto: pontos):

    for _ in range(5):
        ponto.setar_ponto()
        lista.append(ponto)

    return lista


def dominancia(lista1, lista2):

    A = sum(lista1)
    B = sum(lista2)

    if (A < B):
        print("A domina B!")
        print(f"A = {A}")
        print(f"B = {B}")
        return 1
    elif (B < A):
        print("B domina A!")
        print(f"A = {A}")
        print(f"B = {B}")
        return -1
    else:
        print("Ambos não se dominam")
        print(f"A = {A}")
        print(f"B = {B}")
        return 0

    print("")



def verificar_dominancia(pontos:list[pontos], nao_dominados):

    i = 0
    j = 1

    for i in range(len(pontos)):
        nao_dominados.append(pontos[i].elementos)
        for j in range(len(pontos)):

            if pontos[j].marcado == True:
                break

            else:
                if i == j: continue

                if dominancia(pontos[i].elementos, pontos[j].elementos) == -1:
                    nao_dominados.pop()
                    pontos[i].marcado = True
                    j+=1
                    break

    return nao_dominados


cpf = "076.936.965-04"
cpf_only_num = []
for digito in cpf:

    if digito.isdigit():
        cpf_only_num.append(int(digito))

print(*cpf_only_num)
