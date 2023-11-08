def conjuncao(conjuntoATratado, conjuntoBTratado): #recebe os conjuntos tratados  
    conjuncaoResultado = []; #cria um array dos conjuntos
    for elemento in conjuntoATratado: #para cada elemento no conjunto A
        if elemento in conjuntoBTratado: #se existir no conjunto B
            conjuncaoResultado.append(elemento) #adiciona o elemento no resultado
    print(f"Conjuncao: {conjuncaoResultado}")
    return conjuncaoResultado


def disjuncao(conjuntoATratado, conjuntoBTratado): #recebe os conjuntos tratados 
    disjuncaoResultado = set() #cria um objeto para armazenas os elementos do conjunto de forma que nao se repitam 
    for elemento in conjuntoATratado: #percorre o conjunto
        disjuncaoResultado.add(elemento) #adiciona o elemento
    for elemento in conjuntoBTratado:
        disjuncaoResultado.add(elemento)

    disjuncaoResultado = list(disjuncaoResultado) #transforma o objeto em uma lista
    print(f"Disjuncao: {disjuncaoResultado}")
    return disjuncaoResultado

def trataEntrada(conjunto): #retirar espaço do elemento para cada elemento do conjunto separado por virgula
    conjuntoTratado = [elemento.strip() for elemento in conjunto.split(',')] #split separa os elementos por virgula
    return conjuntoTratado  # o strip() retira o espaço de cada elemento dentro do conjunto

loop = 1
while loop == 1:

    conjuntoA = input("Digite o primeiro conjunto, separado por VIRGULAS: ")
    conjuntoB = input("Digite o segundo conjunto, separado por VIRGULAS: ")
    
    conjuntoATratado = trataEntrada(conjuntoA) #chama a funcao para retirar espaços e separar por virgula
    print(f"Conjunto A: ${conjuntoATratado}")
    conjuntoBTratado = trataEntrada(conjuntoB) #chama a funcao para retirar espaços e separar por virgula
    print(f"Conjunto B: ${conjuntoBTratado}")

    conjuncao(conjuntoATratado, conjuntoBTratado)
    disjuncao(conjuntoATratado, conjuntoBTratado)
    loop = int(input("Deseja tentar de novo? 1 - sim | 2 - nao: "))
    while loop != 1 and loop != 2:
        loop = int(input("Insira uma opção válida: 1 - sim | 2 - nao: "))
