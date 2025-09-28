import random
import math
import threading
import time

Lista = []
Lista_func_objetivo = []
Lista_var_decisao = []
minimo = -100.0
maximo = 100.0

def preencher_lista_aleatoria(lista_elem):

    for _ in range(50):
        elem_aleatorio = random.uniform(minimo, maximo)
        lista_elem.append(elem_aleatorio)

    return lista_elem


def rastrigin(lista_elem):
    pi = math.pi
    acc = 0
    for elem in lista_elem:
        acc += (pow(elem, 2) - 10*math.cos(2*pi*elem)+10)
    return acc



def Quality(lista_elem):
    return rastrigin(lista_elem)



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



def tempura_simulada(lista_elem, iteracoes, r, p, t):
    S = lista_elem
    Best = S
    P = 1.0

    while t > 0.05 or iteracoes > 0:
        R = Tweak(S.copy(),p ,r)
        expoente = (Quality(S) - Quality(R)) / t

        if Quality(S) < Quality(R):
            P = math.exp(expoente)  #  e^expoente
        num_random = random.uniform(0.0, 1.0)

        if Quality(R) < Quality(S) or num_random < P:
            S = R
        if Quality(S) < Quality(Best):
            Best = S

        t = max(0.05, t)
        t -= t/iteracoes
        iteracoes -= 1
    return Best



def resultado_final_RS(lista_elem, lista_funcao_objetivo, p, r, t, interacoes):

    preencher_lista_aleatoria(lista_elem)
    for i in range(10):

        resultado = tempura_simulada(lista_elem, interacoes, r, p, t)
        resultado_soma = rastrigin(resultado)

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



print ("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t *************** Lista das variáveis de decisão - Recozimento Simulado Rastrigin *************** \n\n")


#  Valores para interações = 1000, 10000, 50000

#  Valores para p =  0.10,  0.50,   1
#  Valores para r =  0.1,    1,    100
#  Valores para t =  1000,  3000,  5000



resultado_final_RS(Lista, Lista_func_objetivo, 0.10, 0.1, 1000, 1000)
escrita_arq("1-RS_Rastrigin_p=0.10_r=0.1_t=1000_i=1000.txt", Lista_func_objetivo)

resultado_final_RS(Lista, Lista_func_objetivo, 0.50, 1, 3000, 1000)
escrita_arq("1-RS_Rastrigin_p=0.50_r=1_t=3000_i=1000.txt", Lista_func_objetivo)

resultado_final_RS(Lista, Lista_func_objetivo, 1, 100, 5000, 1000)
escrita_arq("1-RS_Rastrigin_p=1_r=100_t=5000_i=1000.txt", Lista_func_objetivo)





resultado_final_RS(Lista, Lista_func_objetivo, 0.10, 0.1, 1000, 10000)
escrita_arq("2-RS_Rastrigin_p=0.10_r=0.1_t=1000_i=10000.txt", Lista_func_objetivo)

resultado_final_RS(Lista, Lista_func_objetivo, 0.50, 1, 3000, 10000)
escrita_arq("2-RS_Rastrigin_p=0.50_r=1_t=3000_i=10000.txt", Lista_func_objetivo)

resultado_final_RS(Lista, Lista_func_objetivo, 1, 100, 5000, 10000)
escrita_arq("2-RS_Rastrigin_p=1_r=100_t=5000_i=10000.txt", Lista_func_objetivo)





resultado_final_RS(Lista, Lista_func_objetivo, 0.10, 0.1, 1000, 50000)
escrita_arq("3-RS_Rastrigin_p=0.10_r=0.1_t=1000_i=50000.txt", Lista_func_objetivo)

resultado_final_RS(Lista, Lista_func_objetivo, 0.50, 1, 3000, 50000)
escrita_arq("3-RS_Rastrigin_p=0.50_r=1_t=3000_i=50000.txt", Lista_func_objetivo)

resultado_final_RS(Lista, Lista_func_objetivo, 1, 100, 5000, 50000)
escrita_arq("3-RS_Rastrigin_p=1_r=100_t=5000_i=50000.txt", Lista_func_objetivo)



#
# thread1 = threading.Thread(target=resultado_total_RS, args=(Lista1, Lista_func_objetivo, 0.10, 0.1, 1000, 1000))
# escrita_arq("1-RS_Rastrigin_p=0.10_r=0.1_t=1000_i=1000.txt", Lista_func_objetivo)
#
# thread2 = threading.Thread(target=resultado_total_RS, args=(Lista2, Lista_func_objetivo, 0.50, 1, 3000, 1000))
# escrita_arq("1-RS_Rastrigin_p=0.50_r=1_t=3000_i=1000.txt", Lista_func_objetivo)
#
# thread3 = threading.Thread(target=resultado_total_RS, args=(Lista3, Lista_func_objetivo, 1, 100, 5000, 1000))
# escrita_arq("1-RS_Rastrigin_p=1_r=100_t=5000_i=1000.txt", Lista_func_objetivo)
#
#
#
#
# thread4 = threading.Thread(target=resultado_total_RS, args=(Lista4, Lista_func_objetivo, 0.10, 0.1, 1000, 10000))
# escrita_arq("2-RS_Rastrigin_p=0.10_r=0.1_t=1000_i=10000.txt", Lista_func_objetivo)
#
# thread5 = threading.Thread(target=resultado_total_RS, args=(Lista5, Lista_func_objetivo, 0.50, 1, 3000, 10000))
# escrita_arq("2-RS_Rastrigin_p=0.50_r=1_t=3000_i=10000.txt", Lista_func_objetivo)
#
# thread6 = threading.Thread(target=resultado_total_RS, args=(Lista6, Lista_func_objetivo, 1, 100, 5000, 10000))
# escrita_arq("2-RS_Rastrigin_p=1_r=100_t=5000_i=10000.txt", Lista_func_objetivo)
#
#
#
# thread7 = threading.Thread(target=resultado_total_RS, args=(Lista7, Lista_func_objetivo, 0.10, 0.1, 1000, 50000))
# escrita_arq("3-RS_Rastrigin_p=0.10_r=0.1_t=1000_i=50000.txt", Lista_func_objetivo)
#
# thread8 = threading.Thread(target=resultado_total_RS, args=(Lista8, Lista_func_objetivo, 0.50, 1, 3000, 50000))
# escrita_arq("3-RS_Rastrigin_p=0.50_r=1_t=3000_i=50000.txt", Lista_func_objetivo)
#
# thread9 = threading.Thread(target=resultado_total_RS, args=(Lista9, Lista_func_objetivo, 1, 100, 5000, 50000))
# escrita_arq("3-RS_Rastrigin_p=1_r=100_t=5000_i=50000.txt", Lista_func_objetivo)
#
# thread1.start()
# thread2.start()
# thread3.start()
# thread4.start()
# thread5.start()
# thread6.start()
# thread7.start()
# thread8.start()
# thread9.start()
#
#
# thread1.join()
# thread2.join()
# thread3.join()
# thread4.join()
# thread5.join()
# thread6.join()
# thread7.join()
# thread8.join()
# thread9.join()

