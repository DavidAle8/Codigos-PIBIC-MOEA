import random
from PIBIC_Parte1 import Sphere
from copy import deepcopy

Lista = []
Lista_func_objetivo = []

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

        self.set_fitness(Sphere.sphere(self.get_genoma()))
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

        Sphere.preencher_lista_aleatorio(genoma)  # Puxando preencher_lista_aleatorio do Sphere
        individuo.set_genoma(genoma)
        lista_elem.append(individuo)

    return lista_elem


def evolution_strategy(populacao, pais, filhos, p, r, interacoes):

    Best = Individuo([], 7976931348623157e+308)
    Q = []
    acc = 0

    gerar_populacao(populacao)
   
    while acc < interacoes:

        for individuo in populacao:

            individuo.assess_fitnes() # Chamar o acumulador 'acc' aq

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


def resultado_total_ES(lista_elem, lista_func_objetivo, pais, filhos, p, r, interacoes):

    gerar_populacao(lista_elem)
    for i in range(10):

        resultado = evolution_strategy(lista_elem, pais, filhos, p, r, interacoes)
        resultado_soma = Sphere.sphere(resultado.get_genoma())

        lista_func_objetivo.append(resultado_soma)
        print(f"{i + 1}°Resultado da soma com {interacoes} interações: {resultado_soma}\n")

    lista_elem.clear()
    print("\n")



def escrita_arq(caminho, lista_elem):

    with open(caminho, "w", encoding="utf-8") as arquivo:

        for i, result in enumerate(lista_elem, 1):

            arquivo.write(str(result))
            arquivo.write("\n")

    lista_elem.clear()



# 3-ES_Sphere_p=0.10_r=0.1_pais=5_filhos=10_i=50000.txt
# 3-ES_Sphere_p=0.50_r=1_pais=15_filhos=100_i=50000.txt
# 3-ES_Sphere_p=1_r=100_pais=25_filhos=250_i=50000.txt


#  Valores para interações = 1000, 10000, 50000
#  Valores para p = 0.10,  0.50,  1
#  Valores para r = 0.1,    1,   100

# pais = 5, 15, 25
# filho = 10, 100, 250


print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t *************** Lista das variáveis de decisão - Evolution Strategy Sphere *************** \n\n")


#  Valores para interações = 1000, 10000, 50000
#  Valores para p = 0.10,  0.50,  1
#  Valores para r = 0.1,    1,   100

# pais = 5, 15, 25
# filho = 10, 100, 250

resultado_total_ES(Lista, Lista_func_objetivo, 5, 10, 0.10, 0.1, 100)
escrita_arq("1-ES_Sphere_p=0.10_r=0.1_pais=5_filhos=10_i=1000.txt", Lista_func_objetivo)

resultado_total_ES(Lista, Lista_func_objetivo, 15, 100, 0.50, 10, 10)
escrita_arq("1-ES_Sphere_p=0.50_r=1_pais=15_filhos=100_i=1000.txt", Lista_func_objetivo)

resultado_total_ES(Lista, Lista_func_objetivo, 25, 250, 1, 100, 4)
escrita_arq("1-ES_Sphere_p=1_r=100_pais=25_filhos=250_i=1000.txt", Lista_func_objetivo)




resultado_total_ES(Lista, Lista_func_objetivo, 5, 10, 0.10, 0.1, 1000)
escrita_arq("2-ES_Sphere_p=0.10_r=0.1_pais=5_filhos=10_i=10000.txt", Lista_func_objetivo)

resultado_total_ES(Lista, Lista_func_objetivo, 15, 100, 0.50, 10, 100)
escrita_arq("2-ES_Sphere_p=0.50_r=1_pais=15_filhos=100_i=10000.txt", Lista_func_objetivo)

resultado_total_ES(Lista, Lista_func_objetivo, 25, 250, 1, 100, 40)
escrita_arq("2-ES_Sphere_p=1_r=100_pais=25_filhos=250_i=10000.txt", Lista_func_objetivo)




resultado_total_ES(Lista, Lista_func_objetivo, 5, 10, 0.10, 0.1, 5000)
escrita_arq("3-ES_Sphere_p=0.10_r=0.1_pais=5_filhos=10_i=50000.txt", Lista_func_objetivo)

resultado_total_ES(Lista, Lista_func_objetivo, 15, 100, 0.50, 10, 500)
escrita_arq("3-ES_Sphere_p=0.50_r=1_pais=15_filhos=100_i=50000.txt", Lista_func_objetivo)

resultado_total_ES(Lista, Lista_func_objetivo, 25, 250, 1, 100, 200)
escrita_arq("3-ES_Sphere_p=1_r=100_pais=25_filhos=250_i=50000.txt", Lista_func_objetivo)
