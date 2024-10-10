import requests # framework de requisição de API
import pandas as pd # framework para criação e manipulação de Dataframes
from io import StringIO # conversor de arquivos text para csv

api = 'FGO0YEX3QWG8VK3K' # chave api/api key
acao = 'ITUB3'  # Ação que os dados serão coletados
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={acao}.SAO&apikey={api}&datatype=csv'   # API

# Requisição 
r = requests.get(url) 

# Conversão de arquivo text para csv
tabela = pd.read_csv(StringIO(r.text))    
print(tabela)





