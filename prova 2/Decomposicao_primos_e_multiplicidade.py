"""Dado um número inteiro positivo, determine a sua decomposição em fatores primos
calculando também a multiplicidade de cada fator."""

#fatores primos = dividir o numero inteiro por um numero primo
#multiplicidade do fator =  quantas vezes esse numero primo consegue dividir até que o resultados seja 1
"""Pegue um número inteiro positivo. Comece dividindo-o pelo menor número primo, que é o 2. 
Continue fazendo isso repetidamente até não ser mais possível. A cada divisão bem-sucedida, 
anote o número primo usado. A quantidade de vezes que você conseguiu dividir pelo mesmo número primo 
é chamada de multiplicidade desse fator primo. Repita o processo com os próximos números primos 
até que seu número seja reduzido a 1."""

def resolve(n):
    fatores_e_multiplicidade = []  # Lista para armazenar os divisores e sua multiplicidade
    divisor = 2  # Começa com o divisor primo 2
    
    while n != 1:  # Enquanto n não for igual a 1, continue o processo de decomposição.
        multiplicidade = 0  # Inicia a multiplicidade para cada divisor primo
            
        while n % divisor == 0:  # Enquanto n for divisível pelo divisor atual (sem resto):
            n = n // divisor  # Reduz n dividindo-o pelo divisor.
            multiplicidade += 1  # Aumenta a multiplicidade do divisor atual.
                
        if multiplicidade > 0:  # Se a multiplicidade for maior que zero, ou seja, o divisor é um fator.
            fatores_e_multiplicidade.append(f"O fator {divisor} tem multiplicidade {multiplicidade}")# Adiciona uma string à lista, indicando o divisor e sua multiplicidade.
            
            divisor += 1  # Incrementa o divisor para verificar o próximo número primo.
    
    return "\n".join(fatores_e_multiplicidade)

while True:
    num = int(input("Insira um número para determinar a sua decomposição em fatores primos calculando também a multiplicidade de cada fator: "))
    if num > 0:
        break
    else:
        print("Digite um numero positivo")

resultado = resolve(num)

print(f"O {num} tem:\n{resultado}")
