def prova_por_inducao(n):
    resposta = ''

    # Base da indução
    resposta += "Base:\n"
    base = n**2 > (5*n) + 10
    resposta += f"{n}^2 > 5*{n} + 10\n"
    resposta += f"{n**2} > {5*n} + 10\n"
    resposta += f"{n**2} > {5*n + 10}\n"
    resposta += f"Base: {base}\n\n"

    if base:
        # Etapa da hipótese
        resposta += "Hipótese: n = k\n"
        resposta += f"k**2 > 5*k + 10\n\n"

        # Etapa da tese
        resposta += "Tese: n = k + 1\n"
        k = n
        resposta += f"Substituir n por k + 1 na hipótese:\n"
        resposta += f"{(k + 1)}^2 > 5*({k + 1}) + 10\n"
        tese_passo1 = (k + 1)**2 > 5*(k + 1) + 10
        resposta += f"{(k + 1)**2} > {5*(k + 1) + 10}\n"
        resposta += f"A tese é: {tese_passo1}\n"

    return resposta

print("Provar por indução finita que n^2 > 5n + 10 para n >= 7")
n = 7
resultado = prova_por_inducao(n)
print(resultado)
