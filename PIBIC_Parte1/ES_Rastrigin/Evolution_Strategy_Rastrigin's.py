import random
from Códigos_PIBIC.PIBIC_Parte1 import Rastrigin
from copy import deepcopy

Lista = []
Lista_func_objetivo = []
Lista_var_decisao = []

maximo = 100.0
minimo = -100.0


class Individuo:
    def __init__(self, genoma, fitness):
        self.genoma = genoma
        self.fitness = fitness


    def mutation(self, p, r):

        genoma = self.get_genoma()
        for i in range(len(genoma)):
            num_random = random.uniform(0.0, 1.0)

            if num_random <= p:
                n = random.uniform(r, -r)
                if minimo <= n + self.get_genoma()[i] <= maximo:
                    genoma[i] += n

        self.set_genoma(genoma)
        return self


    def assess_fitnes(self):  # Setter

        self.set_fitness(Rastrigin.rastrigin(self.get_genoma()))
        return self.fitness


    def get_genoma(self):  #Gett genoma
        return self.genoma


    def set_genoma(self, lista_genoma):  #Sett genoma
        if isinstance(lista_genoma, list):
            self.genoma = lista_genoma
        else:
            raise ValueError("O genoma deve ser uma lista.")


    def get_fitness(self):  #Gett fitness
        return self.fitness


    def set_fitness(self, valor_fitness):  #Gett fitness
        self.fitness = valor_fitness



def gerar_populacao(lista_elem):

    for i in range(50):

        individuo = Individuo([], 7976931348623157e+308)
        genoma = []

        Rastrigin.preencher_lista_aleatorio(genoma)  # Puxando preencher_lista_elem_aleatorio do Sphere
        individuo.set_genoma(genoma)
        lista_elem.append(individuo)

    return lista_elem


def evolution_strategy(populacao, pais, filhos, iteracoes, p, r):
    Best = Individuo([], 7976931348623157e+308)
    Q = []
    acc = 0
    gerar_populacao(populacao)

    while acc < iteracoes:

        for individuo in populacao:
            individuo.assess_fitnes()

            if Best.get_genoma() == [] or individuo.get_fitness() < Best.get_fitness():
                Best = deepcopy(individuo)

        Q.extend(populacao)
        Q.sort(key=lambda individuo: individuo.get_fitness())
        mais_aptos = Q[:pais]

        Q.clear()
        populacao.clear()
 
        for individuo_apto in mais_aptos:
            for _ in range(filhos//pais):

                novo_individuo = deepcopy(individuo_apto)
                novo_individuo.mutation(p, r)
                populacao.append(novo_individuo)

        acc+=1

    return Best


def resultado_final_ES(lista_elem, lista_funcao_objetivo, pais, filhos, interacoes, p, r):

    gerar_populacao(lista_elem)
    for i in range(10):
        resultado = evolution_strategy(lista_elem, pais, filhos, interacoes, p, r)
        resultado_soma = resultado.get_fitness()
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
#  Valores para r = 0.1,  0.5,   1,    50,  100
#  Valores para p = 0.10, 0.25, 0.50, 0.75,  1

# pais = 5, 15, 25
# filho = 10, 100, 250

# "3-ES_Sphere_p=0.10_r=0.1_pais=5_filhos=10_i=50000.txt"
# "3-ES_Sphere_p=0.50_r=1_pais=15_filhos=100_i=50000.txt"
# "3-ES_Sphere_p=1_r=100_pais=25_filhos=250_i=50000.txt"




print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t *************** Lista das variáveis de decisão - Evolution Strategy Rastrigin's *************** \n\n")

resultado_final_ES(Lista, Lista_func_objetivo, 5, 10, 100, 0.10, 0.1)
escrita_arq("1-ES_Rastrigin_p=0.10_r=0.1_pais=5_filhos=10_i=1000.txt", Lista_func_objetivo)

resultado_final_ES(Lista, Lista_func_objetivo, 15, 100, 10, 0.50, 1)
escrita_arq("1-ES_Rastrigin_p=0.50_r=1_pais=15_filhos=100_i=1000.txt", Lista_func_objetivo)

resultado_final_ES(Lista, Lista_func_objetivo, 25, 250, 4, 1, 100)
escrita_arq("1-ES_Rastrigin_p=1_r=100_pais=25_filhos=250_i=1000.txt", Lista_func_objetivo)





resultado_final_ES(Lista, Lista_func_objetivo, 5, 10, 1000, 0.10, 0.1)
escrita_arq("2-ES_Rastrigin_p=0.10_r=0.1_pais=5_filhos=10_i=10000.txt", Lista_func_objetivo)

resultado_final_ES(Lista, Lista_func_objetivo, 15, 100, 100, 0.50, 1)
escrita_arq("2-ES_Rastrigin_p=0.50_r=1_pais=15_filhos=100_i=10000.txt", Lista_func_objetivo)

resultado_final_ES(Lista, Lista_func_objetivo, 25, 250, 40, 1, 100)
escrita_arq("2-ES_Rastrigin_p=1_r=100_pais=25_filhos=250_i=10000.txt", Lista_func_objetivo)





resultado_final_ES(Lista, Lista_func_objetivo, 5, 10, 5000, 0.10, 0.1)
escrita_arq("3-ES_Rastrigin_p=0.10_r=0.1_pais=5_filhos=10_i=50000.txt", Lista_func_objetivo)

resultado_final_ES(Lista, Lista_func_objetivo, 15, 100, 500, 0.50, 1)
escrita_arq("3-ES_Rastrigin_p=0.50_r=1_pais=15_filhos=100_i=50000.txt", Lista_func_objetivo)

resultado_final_ES(Lista, Lista_func_objetivo, 25, 250, 200, 1, 100)
escrita_arq("3-ES_Rastrigin_p=1_r=100_pais=25_filhos=250_i=50000.txt", Lista_func_objetivo)