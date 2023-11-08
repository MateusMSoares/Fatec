#diferença -  Dados os conjuntos A e B: A-B = retirar a interceção de A e B
#Conjunto das partes - cria subconjuntos com todas as possibilidades
from itertools import combinations #Função da biblioteca que gera as combinações automatica

ConjuntoA = [1, 2, 7]
ConjuntoB = [1, 3, 7]

def diferenca(ConjuntoA, ConjuntoB):
    resultado_diferenca = [] #Cria lista para armazenar a diferença
    for elemento in ConjuntoA:
        if elemento not in ConjuntoB: #Se o elemnto de A não estiver e B ele adiciona a diferença
            resultado_diferenca.append(elemento)
    print(f'Diferença entre {ConjuntoA} e {ConjuntoB} é {resultado_diferenca}')

def partes_conjunto(ConjuntoA, ConjuntoB):
    partes_conjuntaA = [] #Cria lista do subconjunto
    partes_conjuntaB = [] #Cria lista do subconjunto

    for i in range(len(ConjuntoA) + 1): #Itera para diferentes tamanhos de subconjuntos de ConjuntoA
        partes_conjuntaA.extend(combinations(ConjuntoA, i))#Gera(combinations) e estende(adiciona o subconjunto gerado) a lista com subconjuntos de tamanho i
    print(f'Partes do Conjunto 1: {partes_conjuntaA}')

    for i in range(len(ConjuntoB) + 1):
        partes_conjuntaB.extend(combinations(ConjuntoB, i))#Itera para diferentes tamanhos de subconjuntos de ConjuntoA
    print(f'Partes do Conjunto 2: {partes_conjuntaB}')

diferenca(ConjuntoA, ConjuntoB)
partes_conjunto(ConjuntoA, ConjuntoB)


