# Codigos-PIBIC-MOEA

Estes códigos fazem parte dos estudos de problemas de otimização multiobjetivo (MOP, do inglês Multi-Objective Optimization Problems) na qual algoritmos multiobjetivo são utilzados para solucioná-los.

# Introdução

A otimização é uma área amplamente pesquisada na ciência da computação,
engenharia e matemática que visa buscar a melhor solução para um problema específico
baseado em critérios bem definidos. Dessa forma, podemos dizer que a área busca
maximizar ou minimizar uma função objetivo respeitando as restrições do problema. Mas,
e se tivéssemos mais de um objetivo a ser avaliado simultaneamente? Os problemas de
otimização multiobjetivo (MOP, do inglês Multi-Objective Optimization Problems) são
uma classe de problemas com dois ou mais funções objetivos a serem otimizados de forma
simultânea, no qual os mesmos podem ter conflitos entre si (COELLO et al., 2007 apud
OLIVEIRA, 2022). Por conta desses conflitos entre os objetivos, não existe apenas uma
melhor solução a ser considerada que possa otimizar totalmente os mesmos, mas sim um
conjunto delas, que chamamos de soluções não-dominadas. Dessa maneira, para obtermos
esse conjunto de soluções, é necessário aplicarmos o que chamamos de Teoria da
Otimalidade de Pareto (COELLO et al., 2007 apud OLIVEIRA, 2022).
Os MOPs são problemas complexos, dessa maneira, Algoritmos Evolutivos
Multiobjetivo (MOEA, do inglês Multi-Objective Evolutionary Algorithm) são algoritmos
inspirados na teoria evolucionária da biológica para busca dos objetivos com maior
aptidão. Estes algoritmos têm se sobressaído e bem aplicados para estes problemas.
Segundo (DÍAZ-MANRÍQUEZ et al., 2016) os MOEAs são técnicas baseadas em
populações que realizam buscas multidimensionais, encontrando mais de uma solução em
uma única execução. Estas técnicas possuem um potencial muito grande quando estamos
falando em buscar soluções próximas dos ótimos globais (soluções próximas das
melhores). Muitos algoritmos que utilizam do conceito da evolução da biologia são
características dos MOEAs. As soluções são indivíduos de uma população, e os mesmos
cruzam entre si para gerar uma população nova. A partir disso os indivíduos sofrem
mutações, e isso auxilia na variabilidade dos mesmos para gerar diferentes soluções nas
próximas gerações.

# Desenvolvimento

A pesquisa separou o desenvolvimento em duas etapas: A primeira foi
estudado e compreendido a implementação de algoritmos mono-objetivo com o
intuito de entender a otimização. E na segunda etapa compreendeu-se a avaliação de
algoritmos surrogates multi-objetivo. A pesquisa não alcançou a implementação de
novos algoritmos, apenas concentrou-se na execução do mesmo no framework
disponibilizado.
Antes de irmos para os algoritmos propriamente ditos, falaremos brevemente
das funções que o compõem para uma melhor demonstração e melhor entendimento.
Nesta pesquisa usamos como função objetivo funções de benchmark da literatura,
sendo elas Sphere e Rastrigin

<img width="344" height="176" alt="image" src="https://github.com/user-attachments/assets/0994ab36-4c85-4af1-8f55-67aeeb9d7eb7" />

## Hill-Climbing

O algoritmo é simples e funciona da seguinte forma: o mesmo recebe uma
lista de 50 elementos como parâmetro (um vetor de números gerados aleatoriamente
entre -100 e 100), uma quantidade de iterações (avaliações), valor da probabilidade
de um número ser alterado (p) e um valor de ruído a ser aplicado (r). Primeiro
fazemos S recebe a nossa lista de elementos atual. Dessa maneira, para cada
avaliação, fazemos uma cópia de S em R aplicando um pequeno ruído em seus
elementos. Se R após o ruído aplicado for melhor que S, então S recebe esta melhor
solução. Como estamos trabalhando com minimização, então a melhor solução será
a menor delas.

## Simulated Annealing

O algoritmo funciona da seguinte forma: Primeiro recebemos uma lista no mesmo
formato que o algoritmo Hill-Climbing, um vetor de 50 elementos variando de -100 a 100.
Copiamos essa lista de elementos para S, Best recebe S para termos uma solução inicial a
ser comparada com as demais e P é o valor de probabilidade que começa alto (100%).
Enquanto a temperatura não esfria (não fica um valor muito pequeno) ou a quantidade de
iterações for maior que 0 (nossas avaliações), rodamos a lógica do algoritmo. Como de
rotina, R recebe uma cópia modificada de S inicialmente e a variável expoente recebe parte
da fórmula que apresentamos da probabilidade P. O algoritmo verifica a condição se
Quality(S) < Quality(R), pois se isso é satisfeito, significa que S é melhor que R, ou seja,
como R é pior, então fazemos o cálculo de probabilidade de P recebendo 𝑃 = 𝑒 (a 𝑒𝑥𝑝𝑜𝑒𝑛𝑡𝑒
ferramenta math.exp do python garante o 𝑒 ). Após isso geramos um valor 𝑒𝑥𝑝𝑜𝑒𝑛𝑡𝑒
num_random aleatório para a verificação de probabilidade e em seguida verificamos a
condição: “se o Quality(R) < Quality(S) ou num_random < P, faça”. Se a condição do if
anterior, Quality(S) < Quality(R) tivesse sido satisfeito antes, então quer dizer que S é
melhor que R, assim, Quality(R) < Quality(S) na condição atual não seria verdadeiro,
sobrando apenas para condição de num random < P para que o comando submisso seja
executado, mas com condição de probabilidade de aceitar soluções ruins baseado no
cálculo da temperatura. Dessa maneira, S recebe o valor ruim de R, guardando soluções
piores. O t = max(0.05, t) significa que o menor valor de t será no mínimo 0,05 e
diminuímos ele subtraindo-o de t/iterações, ou seja, “esfriamos” ele lentamente para
assegurar que a condição de aceitar resultados ruins de R aconteça até que a validade disso
acaba, logo, sobrando apenas para aceitar soluções melhores e colocando em Best na
condição: “se o Quality(S) < Quality(Best)”, assim, Best recebe S e o retornamos.

##  Evolution Strategy

O algoritmo trabalha da seguinte forma: recebemos como parâmetro uma população
de indivíduos, pais que representarão a quantidade de indivíduos aptos para reprodução e
filhos, quantidade de descendentes desses pais. O Best inicialmente recebe o pior
indivíduo possível inicialmente para termos um indivíduo inicial substituível e Q, nossa
lista dos melhores indivíduos, começa vazia inicialmente. Após isso geramos uma
população aleatória, uma lista de 50 indivíduos com um genoma de também tamanho 50
com elementos variando de -100 a 100. Em seguida percorremos cada indivíduo dessa lista
avaliando seu fitness com o assess_fitness e verificando se o fitness do indivíduo que
estamos avaliando agora é melhor que o de Best, se for, Best recebe este indivíduo fazendo
uma cópia dele. Com todas essas avaliações feitas, fazemos Q receber esses indivíduos
avaliados, ordenando eles do menor para o maior, ou seja, do melhor pro pior, e pegamos
os pais melhores e colocamos em uma outra lista dos mais aptos, nesse caso
intuitivamente na lista mais_aptos. A ideia de limpar Q e populacao será para uma
próxima rodada com uma nova geração de indivíduos. E por fim, percorremos cada
indivíduo apto da nossa lista dos mais aptos para gerar indivíduos novos pela quantidade
da expressão filhos//pais (divisão inteira de filhos e pais), ou seja, praticamente, para cada
indivíduo apto da lista, (os pais melhores, digamos assim), é gerado um novo indivíduo
com uma mutação aplicada (um ajuste em seus elementos).

# Resultados

## Resultados Hill-Climbing

<img width="1408" height="454" alt="image" src="https://github.com/user-attachments/assets/a380c098-2d18-452e-b6a0-d098b4bfba35" />

Na tabela podemos ver que, tanto no Sphere quanto no Rastrigin
obtivemos as melhores soluções usando a configuração com iteração =
10000, p = 0.5 e r = 1. O segundo melhor valor de ambas as funções
objetivo se concentraram nas mesmas configurações de p e r, apenas
havendo mudança na quantidade de iterações que foi 50000, porém se
percebermos, não mudou tanto em relação ao primeiro resultado, o que nos
diz que este seria um teto interessante para os melhores resultados
Hill-Climbing com estas configurações. Após isso não obtivemos resultados 
interessantes. Sendo assim, podemos concluir que p = 0.5 e r = 1 foram os
MVPs das melhores soluções, independente do valor de iteração.

## Resultados Simulated Annealing

<img width="1151" height="364" alt="image" src="https://github.com/user-attachments/assets/a60239b2-42e1-49f2-a98d-76422de521e7" />

Para estes resultados, devemos lembrar que o Recozimento Simulado
possui um parâmetro a mais dos que foram definidos, no caso o da
temperatura t que foi configurada da seguinte forma: t = 5000, 3000 e 1000.
Partindo agora para os resultados, podemos ver também que os melhores
deles permearam-se nas configurações de iteração = 50000, p = 0.5, r = 1 e
agora com t = 3000. Como segundo melhor resultado obtivemos com os
mesmos valores de p, r e t mas com iteração = 10000. Porém, perceba
também que, diferente do Hill-Climbing, o Recozimento Simulado melhora
seus resultados à medida que o número de internações cresce. Dessa
maneira, podemos concluir que o Simulated Annealing precisa de mais
explorações para alcançar melhores resultados.

## Resultados Evolution Strategy

E por fim, os resultados do algoritmo Evolution Strategy, que
também possui parâmetros específicos pais e filhos, que foram configurados
da seguinte forma: pais = 5, 15 e 25, e filhos = 10, 100 e 250.

<img width="821" height="296" alt="image" src="https://github.com/user-attachments/assets/3cd39e76-a913-4c78-a8d9-8d54b8a20a1f" />

Diante dos resultados, já podemos visualizar que também tivemos os
melhores resultados nas configurações gerais de iteração = 50000, p = 0.5 e
r = 1, e adicionalmente, as configurações do algoritmo, pais = 15 e filhos =
100. Podemos averiguar também que, o Evolution Strategy, por ser um
algoritmo melhor em buscar as soluções, não obteve o melhor resultado de
todos os algoritmos na função Sphere, mas se saiu melhor com a função
Rastrigin. Seu segundo melhor resultado surgiu nas mesmas configurações,
com a única diferença no valor de iterações, que neste caso ficou em 10000,
e chegou próximo do melhor resultado. Logo, podemos concluir então que o
algoritmo lida melhor com funções mais complexas.

