import tkinter as tk
from tkinter import ttk
import yfinance as yf
from datetime import datetime, timedelta

def obter_valores_acoes():
    simbolos = ['AAPL', 'MSFT', 'AMZN']
    valores = []

    for simbolo in simbolos:
        acao = yf.Ticker(simbolo)
        dados = acao.history(start='2023-01-01', end=datetime.now(), interval='1d')
        
        # Filtra para obter os dados de todo dia 15
        dados_15 = dados[dados.index.day == 15]
        
        if not dados_15.empty:
            ultimo_valor = dados_15['Close'].iloc[-1]
            valores.append((simbolo, ultimo_valor))
        
    return valores

def atualizar_valores():
    dados_acoes = obter_valores_acoes()

    for i, (simbolo, valor) in enumerate(dados_acoes):
        label_valores[i].config(text=f"{simbolo}: ${valor:.2f}")

    root.after(60000, atualizar_valores)  # Atualiza a cada 60 segundos (60000 milissegundos)

# Configuração da janela principal
root = tk.Tk()
root.title("Valores das Ações")
root.geometry("400x200")  # Ajusta o tamanho da janela

# Frame para os rótulos
frame_rotulos = ttk.Frame(root)
frame_rotulos.grid(row=0, column=0, padx=10, pady=5, sticky="w")

# Rótulos para exibir os valores das ações
label_valores = [ttk.Label(frame_rotulos, text="") for _ in range(3)]
for i, label in enumerate(label_valores):
    label.grid(row=i, column=0, pady=5, sticky="w")

# Adiciona uma barra de rolagem à janela principal
scrollbar = ttk.Scrollbar(root, orient="vertical")
scrollbar.grid(row=0, column=1, rowspan=3, sticky="ns")

# Botão para sair
btn_sair = ttk.Button(root, text="Sair", command=root.destroy)
btn_sair.grid(row=1, column=0, pady=10)

# Atualiza os valores iniciais e inicia o loop principal
atualizar_valores()
root.mainloop()
