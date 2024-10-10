import requests # framework de requisição de API
import pandas as pd # framework para criação e manipulação de Dataframes
from io import StringIO # conversor de arquivos text para csv


api = 'FGO0YEX3QWG8VK3K' # chave api / api key
acao = 'ITUB3'

url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={acao}.SAO&apikey={api}&datatype=csv'
r = requests.get(url)

print(r.text)



tabela = pd.read_csv('r.csv')
display(tabela)




