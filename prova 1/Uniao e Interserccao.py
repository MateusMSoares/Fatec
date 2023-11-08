#A uniao siginifica que um conjunto é sub Conjunto de outro.

#A interseccao significa que um conjunto faz a interceccoes
#de alguns ou de todos os seus elemento com um ou mais conjuntos.

inteiros = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
numerosPares = {'0', '2', '4', '8', '10', '12', '14'}
conjuntos = {'inteiros': inteiros, 'numeros Pares': numerosPares}
loop = True

def imprimir_conjunto(numero, conjunto):
    valores_ordenados = ', '.join(sorted(conjunto))
    print(f"{numero} = {valores_ordenados}")

while loop:
    print("Conjuntos Disponíveis: ")
    for i, conjunto in enumerate(conjuntos.keys()):
        imprimir_conjunto(i + 1, conjuntos[conjunto])
    Operacao = input("Digite a operação desejada (ex: 1U2 = união e 2I1 = interseção) ou 3 para inserir um novo conjunto: ")
    Operacao = Operacao.upper()
    
    if Operacao == '3':
            novo_conjunto = input("Digite o novo conjunto separado por vírgulas: ")
            conjuntos["Novo Conjunto"] = set(elemento.strip() for elemento in novo_conjunto.split(','))
            continue
    
    if len(Operacao) != 3:
        print("Digite um formato válido: 2U1 ou 2I1")
        continue  # Volta ao início do loop

    PrimeiroConjunto = int(Operacao[0])
    SegundoConjunto = int(Operacao[2])

    if (PrimeiroConjunto not in range(1, len(conjuntos) + 1)) or (SegundoConjunto not in range(1, len(conjuntos) + 1)):
        print("Digite uma entrada válida: 0, 2, 5, 8")

    conjunto1 = list(conjuntos.values())[PrimeiroConjunto -1]
    conjunto2 = list(conjuntos.values())[SegundoConjunto -1]

    Operador = Operacao[1]
    if Operador == 'U':
        resposta = conjunto1 | conjunto2
    elif Operador == 'I':
        resposta = conjunto1 & conjunto2
    print(resposta)

    loop = input("Deseja tentar novamente? (S ou N) ").strip().upper()
    if loop != 'S':
        loop = False
