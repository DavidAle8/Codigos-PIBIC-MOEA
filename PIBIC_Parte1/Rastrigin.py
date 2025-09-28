import math
import random

Lista = []
lista_resultado1 = []
lista_resultado2 = []
lista_resultado3 = []
minimo = -100.0
maximo = 100.0


def preencher_lista_aleatorio(lista):

    for i in range(50):
        elem_aleatorio = random.uniform(minimo, maximo)  # Números reais
        lista.append(elem_aleatorio)

    return lista


def rastrigin(lista):
    pi = math.pi
    acc = 0

    for elem in lista:
        acc += (pow(elem, 2) - 10*math.cos(2*pi*elem)+10)

    return acc



def tweak(lista, p, r):

    for i in range(len(lista)):
        num_random = random.uniform(0.0, 1.0)

        if num_random < p:

            while True:

               n = random.uniform(-r, r)
               if minimo <= (lista[i] + n) <= maximo:

                   lista[i] += n
                   break
    return lista




def interacoes(lista, lista_resultado, interacao, r, p):

    lista_aux = lista.copy()
    acc_resultados = []

    for _ in range(10):
        for _ in range(interacao):
            lista_aux = tweak(lista, p, r)

        #resultado = f"Lista com {interacao} interações, r = {r} e = p = {p}: {lista_aux}"
        #lista_resultado.append(rastrigin(lista_aux))
    lista_resultado.append(rastrigin(lista_aux))
    resultado = f"Lista com {interacao} interações, r = {r} e = p = {p}: {lista_aux}"
    print(resultado)

    acc_resultados.append(resultado)
    return "\n".join(acc_resultados)



def soma_resultado(lista, interacao):

    acc_resultados = []
    for i in range(len(lista)):

        resultado = f"{i+1}°Resultado da soma de {interacao} interações: {lista[i]}"
        print(resultado)
        acc_resultados.append(resultado)

    return "\n".join(acc_resultados)



def escrever_no_arquivo(caminho, **kwargs):

    with open(caminho, "w", encoding="utf-8") as arquivo:

        for chave, valor in kwargs.items():
            arquivo.write(f"{valor}\n")

        arquivo.write("")



preencher_lista_aleatorio(Lista)

print(f"Lista base: {Lista}")
print(f"Soma da litsa base: {rastrigin(Lista)}\n\n")


#
# print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t *************** Lista das variáveis de decisão - Rastrigin's *************** \n")
#
# escrever_no_arquivo(
#
#     "Variaveis de decisão Hill Climbing Rastrigin's.txt",
#
#     i1_1000=interacoes(Lista, lista_resultado1, 1000, 0.1, 0.10),
#     i2_1000=interacoes(Lista, lista_resultado1, 1000, 0.5, 0.25),
#     i3_1000=interacoes(Lista, lista_resultado1, 1000, 1, 0.50),
#     i4_1000=interacoes(Lista, lista_resultado1, 1000, 50, 0.75),
#     i5_1000=interacoes(Lista, lista_resultado1, 1000, 100, 1),
#
#     espaco1="\n",
#
#     i1_10000=interacoes(Lista, lista_resultado2, 10000, 0.1, 0.10),
#     i2_10000=interacoes(Lista, lista_resultado2, 10000, 0.5, 0.25),
#     i3_10000=interacoes(Lista, lista_resultado2, 10000, 1, 0.50),
#     i4_10000=interacoes(Lista, lista_resultado2, 10000, 50, 0.75),
#     i5_10000=interacoes(Lista, lista_resultado2, 10000, 100, 1),
#
#     espaco2="\n",
#
#     i1_50000=interacoes(Lista, lista_resultado3, 50000, 0.1, 0.10),
#     i2_50000=interacoes(Lista, lista_resultado3, 50000, 0.5, 0.25),
#     i3_50000=interacoes(Lista, lista_resultado3, 50000, 1, 0.50),
#     i4_50000=interacoes(Lista, lista_resultado3, 50000, 50, 0.75),
#     i5_50000=interacoes(Lista, lista_resultado3, 50000, 100, 1),
#
# )
#
# escrever_no_arquivo(
#
#     "Função objetivo Hill Climbing Rastrigin's.txt",
#     result1=soma_resultado(lista_resultado1, 1000),
#     espaco1="\n",
#     result2=soma_resultado(lista_resultado2, 10000),
#     espaco2="\n",
#     result3=soma_resultado(lista_resultado3, 50000)
# )