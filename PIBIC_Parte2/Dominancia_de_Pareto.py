import random

Lista = []
frente_de_pareto = []

def gerar_vetores(lista):

    for _ in range(5):
        
        lista_aux = []
        for num_aleatorio in range(3):

            num_aleatorio = random.randint(0, 1)
            lista_aux.append(num_aleatorio)
            
        lista.append(lista_aux)
 

def dominancia_pareto(lista1, lista2):

    individuo_A = lista1
    individuo_B = lista2

    if (individuo_A > individuo_B):
        print(f"A domina B!")
        print(f"A = {individuo_A}")
        print(f"B = {individuo_B}")
        return 1
    elif(individuo_B < individuo_A):
        print("B domina A!")
        print(f"A = {individuo_A}")
        print(f"B = {individuo_B}")
        return -1
    else:
        print("Ambos não se dominam")
        print(f"A = {individuo_A}")
        print(f"B = {individuo_B}")
        return 0


def verificar_dominancia(lista, nao_dominados):
    
    j = 0
    for i in range(len(lista)):
        j += i+1
        nao_dominados.append(lista[i])
        for j in range(len(lista)):
            if i == j:
                continue

            if dominancia_pareto(lista[i], lista[j]) == -1:
                nao_dominados.pop()
                break

    return nao_dominados

#  [[0, 1, 0], [1, 1, 0], [0, 0, 1], [1, 1, 0], [1, 1, 0]]

gerar_vetores(Lista)


verificar_dominancia(Lista, frente_de_pareto)

print("Elementos da lista: ", Lista)
print("Lista de nao-dominados:",frente_de_pareto)