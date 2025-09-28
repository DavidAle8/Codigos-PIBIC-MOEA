import random
import math
import copy


Lista = []
Lista_func_objetivo = []
minimo = -100.0
maximo = 100.0




def preencher_lista_aleatoria(lista_elem):

    for _ in range(50):
        elem_aleatorio = random.uniform(minimo, maximo)
        lista_elem.append(elem_aleatorio)

    return lista_elem


def sphere(lista_elem):
    acc = 0
    for elem in lista_elem:
        acc += pow(elem, 2)
    return acc


def Quality(lista_elem):
    return sphere(lista_elem)


def Tweak(lista_elem, p, r):

    for i in range(len(lista_elem)):

        num_random = random.uniform(0.0, 1.0)
        if p <= num_random:

            while True:
                n = random.uniform(-r, r)
                if minimo <= n + lista_elem[i] <= maximo:
                    lista_elem[i] += n
                    break

    return lista_elem


def tempura_simulada(lista_elem, interacoes, r, p, t):

    S = copy.deepcopy(lista_elem)
    Best = S
    P = 1.0

    while t > 0.05 or interacoes > 0:
        R = Tweak(copy.deepcopy(S),p ,r)

        if Quality(S) < Quality(R):  # Tentar fazer Quality(S) > Quality(R)
            expoente = (Quality(S) - Quality(R)) / t
            P = math.exp(expoente)  #  e^expoente

        num_random = random.uniform(0.0, 1.0)

        if Quality(R) < Quality(S) or num_random < P:
            S = R

        if Quality(S) < Quality(Best):
            Best = S

        #t *= 0.8
        t -= t/interacoes
        t = max(0.05, t)

        interacoes -= 1

    return Best



def resultado_final_RS(lista_elem, lista_funcao_objetivo, r, p, t, interacoes):

    preencher_lista_aleatoria(lista_elem)
    for i in range(10):

        resultado = tempura_simulada(lista_elem, interacoes, r, p, t)
        resultado_soma = sphere(resultado)

        lista_funcao_objetivo.append(resultado_soma)

        print(f"{i + 1}°Resultado da soma com {interacoes} interações: {resultado_soma}\n")

    lista_elem.clear()
    print("\n")



def escrita_arq(caminho, lista_elem):

    with open(caminho, "w", encoding="utf-8") as arquivo:

        for i, result in enumerate(lista_elem, 1):

            arquivo.write(str(result))
            arquivo.write("\n")

    lista_elem.clear()



#  Valores para interações = 1000, 10000, 50000
#  Valores para r = 0.1,    1,   100
#  Valores para p = 0.10, 0.50,  1
#  Valores para t = 1000, 3000, 5000


print ("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t *************** Lista das variáveis de decisão - Recozimento Simulado Sphere *************** \n\n")


resultado_final_RS(Lista, Lista_func_objetivo, 0.1, 0.10, 1000, 1000)
escrita_arq("1-RS_Sphere_p=0.10_r=0.1_t=1000_i=1000.txt", Lista_func_objetivo)

resultado_final_RS(Lista, Lista_func_objetivo, 1, 0.50, 3000, 1000)
escrita_arq("1-RS_Sphere_p=0.50_r=1_t=3000_i=1000.txt", Lista_func_objetivo)

resultado_final_RS(Lista, Lista_func_objetivo, 100, 1, 5000, 1000)
escrita_arq("1-RS_Sphere_p=1_r=100_t=5000_i=1000.txt", Lista_func_objetivo)



resultado_final_RS(Lista, Lista_func_objetivo, 0.1, 0.10, 1000, 10000)
escrita_arq("2-RS_Sphere_p=0.10_r=0.1_t=1000_i=10000.txt", Lista_func_objetivo)

resultado_final_RS(Lista, Lista_func_objetivo, 1, 0.50, 3000, 10000)
escrita_arq("2-RS_Sphere_p=0.50_r=1_t=3000_i=10000.txt", Lista_func_objetivo)

resultado_final_RS(Lista, Lista_func_objetivo, 100, 1, 5000, 10000)
escrita_arq("2-RS_Sphere_p=1_r=100_t=5000_i=10000.txt", Lista_func_objetivo)



resultado_final_RS(Lista, Lista_func_objetivo, 0.1, 0.10, 1000, 50000)
escrita_arq("3-RS_Sphere_p=0.10_r=0.1_t=1000_i=50000.txt", Lista_func_objetivo)

resultado_final_RS(Lista, Lista_func_objetivo, 1, 0.50, 3000, 50000)
escrita_arq("3-RS_Sphere_p=0.50_r=1_t=3000_i=50000.txt", Lista_func_objetivo)

resultado_final_RS(Lista, Lista_func_objetivo, 100, 1, 5000, 50000)
escrita_arq("3-RS_Sphere_p=1_r=100_t=5000_i=50000.txt", Lista_func_objetivo)

#  Valores para interações = 1000, 10000, 50000
#  Valores para r = 0.1,    1,   100
#  Valores para p = 0.10, 0.50,  1
#  Valores para t = 1000, 3000, 5000

# Para iteração 1000:
# p = 0.10 e r = 0.1
# p = 0.50 e r = 1
# p = 1 e r = 100
#
# Para iteração 10000:
# p = 0.10 e r = 0.1
# p = 0.50 e r = 1
# p = 1 e r = 100
#
# Para iteração 50000:
# p = 0.10 e r = 0.1
# p = 0.50 e r = 1
# p = 1 e r = 100
