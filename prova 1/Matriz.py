#Criando matriz

def criar_matriz_relacao(conjunto, relacoes):
    matriz = [['='] + conjunto]  # rotular as colunas da matriz
    for elemento in conjunto:
        linha = [elemento] + [0] * len(conjunto) # rotular as linhas e adicionar zeros conforme o tamanho do conjunto
        matriz.append(linha)
    print(f"\n 1) Como funciona? Primeira é criado uma lista de listas com os elementos do conjunto adicionando valor zero: \n{matriz}\n")
    print(f"Pense agora que:")
    # Preenche a matriz com 1 onde a relação existe
    for relacao in relacoes:
        elemento1, elemento2 = relacao # pega o elemento de cada relação
    
        indice1 = conjunto.index(elemento1) + 1 # pega o índice do primeiro elemento
        indice2 = conjunto.index(elemento2) + 1 # pega o índice do segundo elemento
        matriz[indice1][indice2] = 1 #linha(a lista dentro da matriz) e coluna(o elemento dentro da matriz)

        print(f" \nPara a relação: ({elemento1}, {elemento2})")
        print(f"Primeiro, verificamos as posições na matriz: [{indice1}][{indice2}]")
        print(f'Se ambos elementos estão presentes na relação, atribuímos o valor 1 à posição [{indice1}][{indice2}]')
        print(f"Assim, a lista {indice1} da matriz e o elemento da lista {indice2} se torna {matriz[indice1]}")
        print(f"Assimilando o valor {matriz[indice1][indice2]} na posição [{indice1}][{indice2}]")

    print('\n')

    return matriz

conjunto = ['A', 'B', 'C', 'D']
relacoes = [('A', 'A'), ('B', 'B'), ('C','C'),('D', 'D')]
print("Criando matriz a partir de uma relação de conjuntos: \n")
print(f"Dado o conjunto: {conjunto} e a relação {relacoes}. \n A sua matriz:")

matriz_relacao = criar_matriz_relacao(conjunto, relacoes)
for linha in matriz_relacao:
    print(' '.join(map(str, linha))) #transforma todos os elementos em strings para que seja possivel concatenar, junta eles separando por espaço