import pandas as pd

dados = {
    'Data': ['01/01/2023', '02/01/2023', '03/01/2023', '04/01/2023', '05/01/2023', '06/01/2023'],
    'Produto': ['Arroz', 'Leite', 'Verduras', 'Feijão', 'Suco', 'Sardinha'],
    'Quantidade': [5, 3, 2, 4, 2, 1],
    'Preco_Unitario': [10, 20, 10, 15, 20, 10],
}

df = pd.DataFrame(dados)

df['Total_Unitario'] = df['Quantidade'] * df['Preco_Unitario']

total_geral = df['Total_Unitario'].sum()

df_total_geral = pd.DataFrame({'Data': ['Total Geral'], 'Produto': [''], 'Quantidade': [''], 'Preco_Unitario': [''], 'Total_Unitario': [total_geral]})
df = pd.concat([df, df_total_geral], ignore_index=True)

df = df.dropna()

print(df)