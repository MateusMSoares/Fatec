import requests
import matplotlib.pyplot as plt
from datetime import datetime

API_KEY = 'f282c56568cb0fc86fed35fdd697f082'
CITY = 'São José Dos Campos'


def buscar_previsao_tempo():
    url_base = 'http://api.openweathermap.org/data/2.5/forecast'
    parametros = {'q': CITY, 'appid': API_KEY, 'units': 'metric'}

    response = requests.get(url_base, params=parametros)
    data = response.json()
    print(data)

    return data['list']

def cria_grafico_previsao(previsao):
    datas = [datetime.fromtimestamp(entrada['dt']) for entrada in previsao]
    temperaturas = [entrada['main']['temp'] for entrada in previsao]

    plt.plot(datas, temperaturas, marker ='o')
    plt.title('Previsão do Tempo para os Próximos 7 Dias em São José dos campos')
    plt.xlabel('Data')
    plt.ylabel('Temperatura (°C)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

previsao = buscar_previsao_tempo()
cria_grafico_previsao(previsao)