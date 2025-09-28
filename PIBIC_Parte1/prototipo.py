import random
import statistics

from Códigos_PIBIC.PIBIC_Parte1.Rastrigin import rastrigin

Lista = []
Lista_func_objetivo = []
Lista_var_decisao = []
dados = []
minimo = -100.0
maximo = 100.0

funcoes = ['Sphere', 'Rastrigin']  # Adicione sua implementação da Rastrigin
iteracoes_config = [1000, 10000, 50000]
parametros = [

    (0.10, 0.1),
    (0.25, 0.5),
    (0.50, 1),
    (0.70, 50),
    (1, 100)
]


def preencher_lista_aleatoria(lista):
    for i in range(50):
        elem_aleatorio = random.uniform(minimo, maximo)
        lista.append(elem_aleatorio)

    return lista


def sphere(lista):
    acc = 0
    for elem in lista:
        acc += pow(elem, 2)
    return acc


def Tweak(lista, p, r):
    for i in range(len(lista)):

        num_random = random.uniform(0.0, 1.0)
        if num_random <= p:
            while True:

                n = random.uniform(-r, r)
                if minimo <= n + lista[i] <= maximo:
                    lista[i] += n
                    break
    return lista



def quality(lista):
    return sphere(lista)



def hill_climbing(lista, interacoes, p, r):
    S = lista

    for _ in range(interacoes):
        R = Tweak(S.copy(), p, r)

        if quality(R) < quality(S):
            S = R

    return S



def resultado_total_HC(lista, lista_func_objetivo, p, r, interacoes):

    resultado = []
    acc = 0
    for _ in range(10):

        resultado = hill_climbing(lista, interacoes, p, r)
        lista_func_objetivo.append(sphere(resultado))

    media = statistics.mean(lista_func_objetivo)
    desvio = statistics.stdev(lista_func_objetivo)

    return {
        'resultados': lista_func_objetivo,
        'media': media,
        'desvio_padrao': desvio
    }


for funcao in funcoes:
    for iteracoes in iteracoes_config:
        for p, r in parametros:
            # Selecionar função objetivo
            if funcao == 'Sphere':
                func_obj = sphere
            elif funcao == 'Rastrigin':
                func_obj = rastrigin  # Implemente esta função

            # Gerar dados
            dados_execucao = gerar_dados_hill_climbing(
                func_obj,
                iteracoes,
                p,
                r
            )

            # Criar entrada na tabela
            linha = {
                'Função': funcao,
                'Iterações': iteracoes,
                'p': p,
                'r': r,
                **{f'Resultado_{i + 1}': val for i, val in enumerate(dados_execucao['resultados'])},
                'Média': dados_execucao['media'],
                'Desvio Padrão': dados_execucao['desvio_padrao']
            }

            dados.append(linha)


def escrita_arq(caminho, lista):
    with open(caminho, "a", encoding="utf-8") as arquivo:

        for i, result in enumerate(lista, 1):

            arquivo.write(result)
            arquivo.write("\n")

            if i % 10 == 0:
                arquivo.write("\n\n\n")

    lista.clear()


preencher_lista_aleatoria(Lista)

print("\t\t\t\t\t\t\t\t\t\t\t\t *************** Lista das variáveis de decisão e função objetivo - Hill Climbing Sphere *************** \n\n\n")

caminho_var_decisao = "Variaveis de decisão Hill Climbing Sphere.txt"
caminho_func_objetivo = "Sphere_p=010_r=01_i=1000.txt"

resultado_total_HC(Lista, Lista_func_objetivo, 0.10, 0.1, 100)
escrita_arq(caminho_func_objetivo, Lista_func_objetivo)

resultado_total_HC(Lista, Lista_func_objetivo, 0.25, 0.5, 100)
escrita_arq(caminho_func_objetivo, Lista_func_objetivo)

resultado_total_HC(Lista, Lista_func_objetivo, 0.50, 1, 100)
escrita_arq(caminho_func_objetivo, Lista_func_objetivo)

resultado_total_HC(Lista, Lista_func_objetivo, 0.75, 50, 100)
escrita_arq(caminho_func_objetivo, Lista_func_objetivo)

resultado_total_HC(Lista, Lista_func_objetivo, 1, 100, 100)
escrita_arq(caminho_func_objetivo, Lista_func_objetivo)




resultado_total_HC(Lista, Lista_func_objetivo, 0.10, 0.1, 1000)
escrita_arq(caminho_func_objetivo, Lista_func_objetivo)

resultado_total_HC(Lista, Lista_func_objetivo, 0.25, 0.5, 1000)
escrita_arq(caminho_func_objetivo, Lista_func_objetivo)

resultado_total_HC(Lista, Lista_func_objetivo, 0.50, 1, 1000)
escrita_arq(caminho_func_objetivo, Lista_func_objetivo)

resultado_total_HC(Lista, Lista_func_objetivo, 0.75, 50, 1000)
escrita_arq(caminho_func_objetivo, Lista_func_objetivo)

resultado_total_HC(Lista, Lista_func_objetivo, 1, 100, 1000)
escrita_arq(caminho_func_objetivo, Lista_func_objetivo)




resultado_total_HC(Lista, Lista_func_objetivo, 0.10, 0.1, 5000)
escrita_arq(caminho_func_objetivo, Lista_func_objetivo)

resultado_total_HC(Lista, Lista_func_objetivo, 0.25, 0.5, 5000)
escrita_arq(caminho_func_objetivo, Lista_func_objetivo)

resultado_total_HC(Lista, Lista_func_objetivo, 0.50, 1, 5000)
escrita_arq(caminho_func_objetivo, Lista_func_objetivo)

resultado_total_HC(Lista, Lista_func_objetivo, 0.75, 50, 5000)
escrita_arq(caminho_func_objetivo, Lista_func_objetivo)

resultado_total_HC(Lista, Lista_func_objetivo, 1, 100, 5000)
escrita_arq(caminho_func_objetivo, Lista_func_objetivo)