#Coursera Estatisticas para analise financeira com python
# pip install pandas
# pip install matplotlib
import pandas as pd
import matplotlib.pyplot as plt
"""usaremos arquivo CSV contendo informacoes sobre acoes do facebook, afim de aprender o basico sobre manipulação de dados com PANDAS"""

facebook = pd.read_csv('facebook.csv')
facebook_enriquecido = facebook.copy()
# print(facebook.head())
# print(f'Linha e colunas: {facebook.shape}')
"""
Quantidade de linhas e colunas -> (780, 7)
"""
# print(facebook.describe())
"""
             Open        High         Low       Close   Adj Close        Volume
count  780.000000  780.000000  780.000000  780.000000  780.000000  7.800000e+02 // linhas preenchidas
mean    80.212705   81.285654   79.022397   80.264897   79.914215  1.204453e+07 // Valor médio
std     64.226121   65.048907   63.190963   64.198375   64.327846  8.221848e+06 // Desvio padrao(o quanto o valor oscila pra + e -)
min     19.250000   19.500000   18.940001   19.139999   18.576082  1.311200e+06 // Valor minimo
25%     25.525000   26.085000   24.845000   25.475000   25.134512  7.215200e+06 // 25% dos valores estão abaixo desse
50%     53.379999   54.034999   52.930000   53.420000   53.035403  9.728700e+06 // 50% dos valores estão abaixo desse
75%    113.322502  115.779999  110.297499  113.702501  113.261238  1.408885e+07 // 75% dos valores estão abaixo desse
max    245.770004  249.270004  244.449997  246.850006  246.850006  9.232320e+07 // Valor mais alto
"""

preco_fechamento_futuro = facebook.copy()
preco_fechamento_futuro['Close price of tommorow'] = facebook[['Close']].shift(-1)
# print(preco_fechamento_futuro)

diferenca_preco = preco_fechamento_futuro.copy()
diferenca_preco['PriceDiff'] = preco_fechamento_futuro['Close price of tommorow'] - facebook['Close'] 


retorno_diario = diferenca_preco.copy()
retorno_diario['Return'] = diferenca_preco['PriceDiff'] / facebook['Close']

direcao = retorno_diario.copy()
direcao['Direction'] = [1 if retorno_diario.loc[varInterar, 'PriceDiff'] > 0 else -1 for varInterar in retorno_diario.index]
"""Compreensão de lista e Operador ternario São usados para criar essa nova coluna:
1 se a condicao for satisfeita -1 se nao.
Uma variavel é criada para iterar sobre cada linha da coluna PriceDiff"""
# print(direcao)

media_movel = retorno_diario.copy()
'''Media movel em 3 dias
shift desce os valores 1 amanha, 2 depois de amanha'''
media_movel['Average 3 days'] = (retorno_diario['Close'] + retorno_diario['Close'].shift(1) + retorno_diario['Close'].shift(2))/3
# print(media_movel)

"""Calcular media movel usando rolling
MA = moving average
"""
facebook_MA = facebook.copy()
facebook_MA["MA40"] = facebook_MA['Close'].rolling(40).mean()
facebook_MA["MA200"] = facebook_MA['Close'].rolling(200).mean()
# print(facebook_MA)

"""Gerar grafico com Pandas e matplotlib"""
plt.subplot(2, 2, 1) # Cria matriz 2x2 sendo o terceiro numero a i
facebook_MA['Close'].plot(legend=True)
facebook_MA['MA40'].plot(legend=True)
facebook_MA['MA200'].plot(legend=True)
plt.title("Diferença entre 40 e 200 dias")

"""Sinal rapido e sinal lento:
MA = moving average
Se a media movel MA10 > MA50 = Compre e mantenha as ações
"""
sinal_rapido_lento = preco_fechamento_futuro.copy()
plt.subplot(2, 2, 2)
sinal_rapido_lento['MA10'] = sinal_rapido_lento['Close'].rolling(10).mean()
sinal_rapido_lento['MA50'] = sinal_rapido_lento['Close'].rolling(50).mean()
sinal_rapido_lento['MA10'].plot(legend=True)
sinal_rapido_lento['MA50'].plot(legend=True)
plt.title("Diferença entre 10 e 50 dias")


"""Adiciona 1 se a acao foi comprada no dia e 0 se nao"""
sinal_rapido_lento['Compra'] = [1 if sinal_rapido_lento.loc[linha, 'MA10'] > sinal_rapido_lento.loc[linha, 'MA50'] else 0 for linha in sinal_rapido_lento.index]
# print(sinal_rapido_lento)


"""Lucro Diario:
Faz o preco do fechamento amanha menos preco do fechamento de hoje, 
caso tenha sido feito compra da açao(Compra == 1)"""
lucro_diario = sinal_rapido_lento.copy()
lucro_diario['Profit'] = [lucro_diario.loc[linha, "Close price of tommorow"] - lucro_diario.loc[linha, 'Close'] if 
                          lucro_diario.loc[linha, 'Compra'] == 1 else 0 for linha in lucro_diario.index] 
# print(lucro_diario)
plt.subplot(2, 2, 3)
lucro_diario['Profit'].plot()
plt.axhline(y=0, color="red")
plt.title('Lucro sobre as acoes vendidas')

"""Lucro acumulado:
soma acumulativa do lucro
"""
lucro_acumulado = lucro_diario.copy()
lucro_acumulado['Wealth'] = lucro_diario['Profit'].cumsum()
plt.subplot(2, 2, 4)
lucro_acumulado['Wealth'].plot()
plt.title("Lucro Acumulado ações vendidas")

print(lucro_acumulado)
print(lucro_acumulado.describe())
print("Total de dinheiro ganho: ", lucro_acumulado.loc[lucro_acumulado.index[-2], 'Wealth'])
print("Total de dinheiro gasto: ", lucro_acumulado.loc[lucro_acumulado.index[0], 'Close'])

plt.tight_layout()
plt.show()