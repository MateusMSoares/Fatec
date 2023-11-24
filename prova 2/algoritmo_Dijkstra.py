# Definindo a funçao Dijkstra para encontrar o caminho mais curto em um grafo ponderado.
def dijkstra(grafo, inicio):
    # Inicializando um conjunto de vertices do grafo.
    vertices = set(grafo.keys())
    print(f'Vertices iniciais{vertices}')
    
    # Inicializando um dicionario de distancias, configurando todas as distancias iniciais como infinito.
    distancias = {vertex: float('infinity') for vertex in vertices}
    print(f'Distancias iniciais: {distancias}')
    
    # A distância do vertice de início para ele mesmo é zero.
    distancias[inicio] = 0
    
    # Conjunto para rastrear os vertices já visitados.
    visitado = set()

    # Enquanto houver vertices não visitados.
    while vertices:
        # Inicializa com um valor grande para garantir que qualquer distância encontrada será menor.
        menor_distancia = float('inf')
        vertex_atual = None
        
        # Encontra o vértice com a menor distância conhecida.
        for vertex in vertices:
            if distancias[vertex] < menor_distancia:
                menor_distancia = distancias[vertex]
                vertex_atual = vertex
        print(f"Vertice atual: {vertex_atual}")

        # Restante do código permanece o mesmo...
        for vizinho, peso in grafo[vertex_atual].items():
            distancia = distancias[vertex_atual] + peso
            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia
        print(f"Vertice: {vertex_atual}, Vertice vizinho: {vizinho}, Distancia: {distancia}")


        visitado.add(vertex_atual)
        print(f"Visitado: {visitado}")
        vertices.remove(vertex_atual)

    return distancias

# Definindo o grafo como um dicionário de dicionários representando as arestas.
grafo = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

inicio = 'A'

resultados = dijkstra(grafo, inicio)

print(f'Distâncias mais curtas a partir de {inicio}: {resultados}')