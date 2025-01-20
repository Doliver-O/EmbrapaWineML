import requests
from bs4 import BeautifulSoup
import csv
from flask import jsonify, request


def fetch_producao_data(ano):
    """
    Realiza scraping da tabela de produção para o ano especificado.
    Retorna os dados da tabela como uma lista de dicionários.
    """
    url = f'http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao=opt_02'
    
    response = requests.get(url)
    print(response)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

   
    table = soup.find('table', {'class': 'tb_base tb_dados'})

    if not table:
        return {"error": "Tabela não encontrada na página."}

    headers = [th.text.strip() for th in table.find_all('th')]
    rows = table.find_all('tr')[1:] 

    data = []
    for row in rows:
        cols = [td.text.strip() for td in row.find_all('td')]
        data.append(dict(zip(headers, cols)))

    return data


def fetch_comerci_data(ano):
    """
    Realiza scraping da tabela de comercialização para o ano especificado.
    Retorna os dados da tabela como uma lista de dicionários.
    """
    url = f'http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao=opt_04'
    
    response = requests.get(url)
    print(response)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

 
    table = soup.find('table', {'class': 'tb_base tb_dados'})

    if not table:
        return {"error": "Tabela não encontrada na página."}

    headers = [th.text.strip() for th in table.find_all('th')]
    rows = table.find_all('tr')[1:] 

    data = []
    for row in rows:
        cols = [td.text.strip() for td in row.find_all('td')]
        data.append(dict(zip(headers, cols)))

    return data




