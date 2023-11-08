conjuntoA = [[1,2],[2,3],[3,4]]

def fechoTransitivo(conjuntos):
    """Inspirado no algoritmo de warshall"""
    maior_valor = 0
    for sublista in conjuntos:
        for elemento in sublista:
            if elemento > maior_valor:
                maior_valor = elemento
    n = maior_valor + 1 
    # criar uma lista com n + 1 posicoes, for é usado para criar copias dessa lista n + 1 vezes(compreensao de lista)
    matriz_adjacencia = [[0] * (n + 1) for _ in range(n + 1)]
    
    for conjunto in conjuntos:
        """matriz_adjacencia[1][2] é 1, o que significa que há uma relação direta do vértice 1 para o vértice 2.
            matriz_adjacencia[2][3] é 1, o que significa que há uma relação direta do vértice 2 para o vértice 3.
            matriz_adjacencia[3][4] é 1, o que significa que há uma relação direta do vértice 3 para o vértice 4."""
        matriz_adjacencia[conjunto[0]][conjunto[1]] = 1

    # Calcule o fecho transitivo usando o algoritmo de Warshall
    for k in range(1, n + 1):
        #Percorre todos os vertices
        for i in range(1, n + 1):
            #verifica se tem relacao entre k e i
            for j in range(1, n + 1):
                #verifica se tem relacao entre k e j
                # Verifica se há um caminho de i para j passando por k e atualiza a matriz de adjacência.
                # Se já existe um caminho direto de i para j (matriz_adjacencia[i][j] é 1) ou se há um caminho direto
                # de i para k (matriz_adjacencia[i][k] é 1) e um caminho direto de k para j (matriz_adjacencia[k][j] é 1),
                # então atualiza a matriz de adjacência para indicar a existência de um caminho direto ou indireto de i para j.
                matriz_adjacencia[i][j] = matriz_adjacencia[i][j] or (matriz_adjacencia[i][k] and matriz_adjacencia[k][j])
    
    resultado = []
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if matriz_adjacencia[i][j]:
                resultado.append([i, j])
    return resultado

fecho_transitivo = fechoTransitivo(conjuntoA)
print(fecho_transitivo)