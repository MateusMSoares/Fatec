#Criando matriz

def criar_matriz_relacao(conjunto, relacoes):
    matriz = [[''] + conjunto]  # primeira linha com os elementos do conjunto
    for elemento in conjunto:
        linha = [elemento] + [0] * len(conjunto)
        matriz.append(linha)

    # preenche a matriz com 1 onde a relação existe
    for relacao in relacoes:
        elemento1, elemento2 = relacao
        indice1 = conjunto.index(elemento1) + 1
        indice2 = conjunto.index(elemento2) + 1
        matriz[indice1][indice2] = 1

    return matriz

conjunto = ['A', 'B', 'C', 'D']
relacoes = [('A', 'B'), ('A', 'C'), ('B', 'C')]

matriz_relacao = criar_matriz_relacao(conjunto, relacoes)

for linha in matriz_relacao:
    print(' '.join(map(str, linha)))
