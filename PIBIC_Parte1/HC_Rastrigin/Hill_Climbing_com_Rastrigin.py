import random
import math

Lista = []
Lista_func_objetivo = []
Lista_var_decisao = []

minimo = -100.0
maximo = 100.0


def preencher_lista_aleatoria(lista_elem):  

    for i in range(50):
        elem_aleatorio = random.uniform(minimo, maximo)
        lista_elem.append(elem_aleatorio)
    return lista_elem



def rastrigin(lista_elem):
    pi = math.pi
    acc = 0

    for elem in lista_elem:
        acc += (pow(elem, 2) - 10*math.cos(2*pi*elem)+10)
    return acc



def Tweak(lista_elem, p, r):

    for i in range(len(lista_elem)):
        num_random = random.uniform(0.0, 1.0)
        if num_random < p:
            while True:
               n = random.uniform(-r, r)
               if minimo <= (lista_elem[i] + n) <= maximo:

                   lista_elem[i] += n
                   break
    return lista_elem


def quality(lista_elem):
    return rastrigin(lista_elem)


def hill_climbing(lista_elem, p, r, interacoes):

    S = lista_elem

    for _ in range(interacoes):
        R = Tweak(S.copy(), p, r)

        if quality(R) < quality(S):
            S = R
    return S



def resultado_total_RS(lista_elem, lista_func_objetivo, p, r, interacoes):

    preencher_lista_aleatoria(Lista)

    for i in range(10):

        resultado = hill_climbing(lista_elem, p, r, interacoes)
        print (resultado)
        resultado_soma = rastrigin(resultado)

        lista_func_objetivo.append(resultado_soma)
        print(f"{i + 1}°Resultado da soma com {interacoes} interações: {resultado_soma}\n")

    print("\n")




def escrita_arq(caminho, lista_elem):

    with open(caminho, "w", encoding="utf-8") as arquivo:

        for i, result in enumerate(lista_elem, 1):

            arquivo.write(str(result))
            arquivo.write("\n")

    lista_elem.clear()



print ("\t\t\t\t\t\t\t\t\t\t\t\t *************** Lista das variáveis de decisão e função objetivo - Hill Climbing rastrigin's *************** \n\n\n")

#  Valores para interações = 1000, 10000, 50000
#  Valores para r = 0.1,  0.5,   1,    50,  100
#  Valores para p = 0.10, 0.25, 0.50, 0.75,  1

# 1-Rastrigin_p=0.10_r=0.1_i=1000.txt
# 1-Rastrigin_p=0.50_r=1_i=1000.txt
# 1-Rastrigin_p=1_r=100_i=1000.txt



resultado_total_RS(Lista, Lista_func_objetivo, 0.10, 0.1, 1000)
escrita_arq("1-HC_Rastrigin_p=0.10_r=0.1_i=1000.txt", Lista_func_objetivo)

resultado_total_RS(Lista, Lista_func_objetivo, 0.50, 1, 1000)
escrita_arq("1-HC_Rastrigin_p=0.50_r=1_i=1000.txt", Lista_func_objetivo)

resultado_total_RS(Lista, Lista_func_objetivo, 1, 100, 1000)
escrita_arq("1-HC_Rastrigin_p=1_r=100_i=1000.txt", Lista_func_objetivo)





resultado_total_RS(Lista, Lista_func_objetivo, 0.10, 0.1, 10000)
escrita_arq("2-HC_Rastrigin_p=0.10_r=0.1_i=10000.txt", Lista_func_objetivo)

resultado_total_RS(Lista, Lista_func_objetivo, 0.50, 1, 10000)
escrita_arq("2-HC_Rastrigin_p=0.50_r=1_i=10000.txt", Lista_func_objetivo)

resultado_total_RS(Lista, Lista_func_objetivo, 1, 100, 10000)
escrita_arq("2-HC_Rastrigin_p=1_r=100_i=10000.txt", Lista_func_objetivo)





resultado_total_RS(Lista, Lista_func_objetivo, 0.10, 0.1, 50000)
escrita_arq("3-HC_Rastrigin_p=0.10_r=0.1_i=50000.txt", Lista_func_objetivo)

resultado_total_RS(Lista, Lista_func_objetivo, 0.50, 1, 50000)
escrita_arq("3-HC_Rastrigin_p=0.50_r=1_i=50000.txt", Lista_func_objetivo)

resultado_total_RS(Lista, Lista_func_objetivo, 1, 100, 50000)
escrita_arq("3-HC_Rastrigin_p=1_r=100_i=50000.txt", Lista_func_objetivo)






#
# def resultado_total_HCRT(lista, p, r, interacoes, media, desvio):
#
#     resultado = []
#     lista_func_objetivo = []
#     for i in range(10):
#
#         resultado[i].append(hill_climbing(lista, interacoes, p, r))  # Guarda os 10 S's das listas da função objetivo
#         lista_func_objetivo.append(rastrigin(resultado[i])) # guarda os valores das funções objetivos das 10 execuções
#
#     media.append(statistics.mean(lista_func_objetivo))  # guarda a média de todos os 10 valores da fun. objetivo daquela config.
#     desvio.append(statistics.stdev(lista_func_objetivo))  # guarda a desvio padrao de todos os 10 valores da fun. objetivo daquela config.
#
#     return {
#         "resultados": lista_func_objetivo,
#         "media HC-rastrigin": media,
#         "desvio_padrao HC-sphere": desvio
#     }
#
