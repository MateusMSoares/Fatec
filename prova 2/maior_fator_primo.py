#Enconta maior fator primo de um numero

def maior_numero_primo(numero):
    num_original = numero

    if numero < 2:
        return f"O numero {num_original} deve ser maior do que 2"
    
    fator = "Não há"

    for i in range(2, numero + 1):
        if numero == 1:
            break
        elif numero % i != 0:
            continue

        fator = f"Maior primo divisivel por {num_original} é {i}"

        #Decomponhe afim de achar o maior fator primo. ex: numero = 45
        # 45 / 3 = 15
        # 15 / 3 = 5
        # 5 / 5 = 1
        while numero % i == 0:
            numero = numero / i

    return fator


numero = int(input("Digite um numero inteiro para saber seu maior fator primo: "))

resultado = maior_numero_primo(numero)
print(resultado)