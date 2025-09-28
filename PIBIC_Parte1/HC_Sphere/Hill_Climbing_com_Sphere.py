import random

Lista = []
Lista_funcao_objetivo = []
Lista_var_decisao = []

minimo = -100.0
maximo = 100.0


def preencher_lista_aleatoria(lista_elem):
    for i in range(50):
        elem_aleatorio = random.uniform(minimo, maximo)
        lista_elem.append(elem_aleatorio)

    return lista_elem


def sphere(lista_elem):
    acc = 0
    for elem in lista_elem:
        acc += pow(elem, 2)
    return acc



def Tweak(lista_elem, p, r):
    for i in range(len(lista_elem)):

        num_random = random.uniform(0.0, 1.0)
        if num_random <= p:
            while True:
                n = random.uniform(-r, r)
                if minimo <= n + lista_elem[i] <= maximo:
                    lista_elem[i] += n
                    break
    return lista_elem



def quality(lista_elem):
    return sphere(lista_elem)



def hill_climbing(lista_elem, iteracoes, p, r):
    S = lista_elem
    for _ in range(iteracoes):
        R = Tweak(S.copy(), p, r)
        if quality(R) < quality(S):
            S = R
    return S



def imprime_console_sp(lista_elem, lista_funcao_objetivo, p, r, interacoes):

    preencher_lista_aleatoria(lista_elem)
    for i in range(10):

        resultado = hill_climbing(lista_elem, interacoes, p, r)
        resultado_soma = sphere(resultado)

        lista_funcao_objetivo.append(resultado_soma)

        print(f"{i + 1}°Resultado da soma com {interacoes} interações: {resultado_soma}\n")

    print("\n")



def escrita_arq(caminho, lista_elem):

    with open(caminho, "w", encoding="utf-8") as arquivo:

        for i, result in enumerate(lista_elem, 1):

            arquivo.write(str(result))
            arquivo.write("\n")

    lista_elem.clear()


print( "\t\t\t\t\t\t\t\t\t\t\t\t *************** Lista das variáveis de decisão e função objetivo - Hill Climbing Sphere *************** \n\n\n")

#  Valores para interações = 1000, 10000, 50000
#  Valores para r = 0.1,   1,    100
#  Valores para p = 0.10, 0.50,   1


imprime_console_sp(Lista, Lista_funcao_objetivo, 0.10, 0.1, 1000)
escrita_arq("1-HC_Sphere_p=0.10_r=0.1_i=1000.txt", Lista_funcao_objetivo)

imprime_console_sp(Lista, Lista_funcao_objetivo, 0.50, 1, 1000)
escrita_arq("1-HC_Sphere_p=0.50_r=1_i=1000.txt", Lista_funcao_objetivo)

imprime_console_sp(Lista, Lista_funcao_objetivo, 1, 100, 1000)
escrita_arq("1-HC_Sphere_p=1_r=100_i=1000.txt", Lista_funcao_objetivo)





imprime_console_sp(Lista, Lista_funcao_objetivo, 0.10, 0.1, 10000)
escrita_arq("2-HC_Sphere_p=0.10_r=0.1_i=10000.txt", Lista_funcao_objetivo)

imprime_console_sp(Lista, Lista_funcao_objetivo, 0.50, 1, 10000)
escrita_arq("2-HC_Sphere_p=0.50_r=1_i=10000.txt", Lista_funcao_objetivo)

imprime_console_sp(Lista, Lista_funcao_objetivo, 1, 100, 10000)
escrita_arq("2-HC_Sphere_p=1_r=100_i=10000.txt", Lista_funcao_objetivo)





imprime_console_sp(Lista, Lista_funcao_objetivo, 0.10, 0.1, 50000)
escrita_arq("3-HC_Sphere_p=0.10_r=0.1_i=50000.txt", Lista_funcao_objetivo)

imprime_console_sp(Lista, Lista_funcao_objetivo, 0.50, 1, 50000)
escrita_arq("3-HC_Sphere_p=0.50_r=1_i=50000.txt", Lista_funcao_objetivo)


imprime_console_sp(Lista, Lista_funcao_objetivo, 1, 100, 50000)
escrita_arq("3-HC_Sphere_p=1_r=100_i=50000.txt", Lista_funcao_objetivo)





#
# def resultado_total_HCSP(lista, p, r, iteracoes, media, desvio):
#
#     lista_func_objetivo = []
#     for i in range(10):
#
#         resultado = hill_climbing(lista, iteracoes, p, r)  # Guarda os 10 S's das listas da função objetivo
#         lista_func_objetivo.append(sphere(resultado)) # guarda os valores das funções objetivos das 10 execuções
#
#     media.append(statistics.mean(lista_func_objetivo))  # guarda a média de todos os 10 valores da fun. objetivo daquela config.
#     desvio.append(statistics.stdev(lista_func_objetivo))  # guarda a desvio padrao de todos os 10 valores da fun. objetivo daquela config.
#
#     return{
#         "resultados": lista_func_objetivo,
#         "media HC-sphere": media,
#         "desvio_padrao HC-sphere": desvio
#     }
#
