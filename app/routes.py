from flask import Blueprint, render_template, jsonify,request,send_file, Flask
from .utils import fetch_producao_data, fetch_comerci_data
from app.utils import fetch_producao_data
import os
import requests
from bs4 import BeautifulSoup
import csv
import io
import jwt
import datetime
from functools import wraps
import jwt
from flask_login import login_user, login_required
from models import User


main = Blueprint('main', __name__)


@main.route('/login', methods=['POST'])
def login():

    username = request.form.get('username')
    password = request.form.get('password')

    if  username == 'admin@teste' and password == 'senha123':
        login_user(User(username))
        return render_template('index.html', title='inicial')



@main.route('/')
def index():
    return render_template('index.html', title='Página Inicial')

@main.route('/login')
def about():
    return render_template('login.html', title='Sobre')


## --------------------------------------------------------------------P R O D U Ç Ã O--------------------------------------------------------------------------- ##

@main.route('/producao')
@login_required
def production():
    return render_template('production.html', title='Produção')

@main.route('/api/producao', methods=['GET'])
@login_required
def api_producao():
    """
    Endpoint para retornar os dados da tabela de produção para o ano especificado.
    """
    ano = request.args.get('ano', '2023')  # Define 2023 como ano padrão
    try:
        data = fetch_producao_data(ano)
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@main.route('/producao/<int:ano>', methods=['GET'])
@login_required
def producao_por_ano(ano):
    """
    Endpoint para buscar dados de produção de acordo com o ano.
    """
    try:
     
        url = f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao=opt_02"


        response = requests.get(url)
        response.raise_for_status()  

      
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table', {'class': 'tb_base tb_dados'})

   
        rows = []
        if table:
            for row in table.find_all('tr'):
                cols = [col.text.strip() for col in row.find_all('td')]
                if cols:
                    rows.append(cols)

     
        return jsonify({'ano': ano, 'dados': rows})

    except Exception as e:
        return jsonify({'erro': str(e)}), 500
    

@main.route('/producao_csv', methods=['GET'])
@login_required
def producao_csv():
    """
    Endpoint que baixa o CSV da produção e retorna os dados em formato JSON.
    """
    csv_url = "http://vitibrasil.cnpuv.embrapa.br/download/Producao.csv"

    try:
  
        response = requests.get(csv_url)
        response.raise_for_status()  

      
        decoded_content = response.content.decode('utf-8')
        csv_reader = csv.reader(io.StringIO(decoded_content), delimiter=';')

     
        dados = []
        headers = None
        for row in csv_reader:
            if headers is None:
                headers = row 
            else:
                dados.append(dict(zip(headers, row)))

        return jsonify({'dados': dados}), 200

    except requests.exceptions.RequestException as e:
        return jsonify({'erro': f'Erro ao acessar o CSV: {str(e)}'}), 500
    
## --------------------------------------------------------------------P R O C E S S A M E N T O----------------------------------------------------------------- ##

@main.route('/processamento')
@login_required
def processamento():
    return render_template('processamento.html', title='Processamento')

@main.route('/api/processamento', methods=['GET'])
@login_required
def processamento_por_ano_opcao():
    try:
        ano = request.args.get('ano', type=int)
        opcao = request.args.get('opcao', type=str)

        if not ano or not opcao:
            return jsonify({'erro': 'Parâmetros "ano" e "opcao" são obrigatórios.'}), 400

        url = f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao=opt_03&subopcao={opcao}"
        
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table', {'class': 'tb_base tb_dados'})

        rows = []
        if table:
            for row in table.find_all('tr'):
                cols = [col.text.strip() for col in row.find_all('td')]
                if cols:
                    rows.append(cols)

        return jsonify({'ano': ano, 'opcao': opcao, 'dados': rows})

    except requests.exceptions.RequestException as e:
        return jsonify({'erro': f'RequestException: {str(e)}'}), 500

    except Exception as e:
        return jsonify({'erro': f'Erro interno: {str(e)}'}), 500
    
@main.route('/processamento_csv', methods=['GET'])
@login_required
def processamento_csv():
    """
    Endpoint que baixa o CSV de processamento e retorna os dados em formato JSON.
    """
    csv_url = "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaAmericanas.csv"

    try:
      
        response = requests.get(csv_url)
        response.raise_for_status()  

   
        decoded_content = response.content.decode('utf-8')
        csv_reader = csv.reader(io.StringIO(decoded_content), delimiter=';')

        dados = []
        headers = None
        for index, row in enumerate(csv_reader):
            if index == 0:
               
                headers = [header.strip() for header in row]
            else:
                
                if any(cell.strip() for cell in row):
                   
                    while len(row) < len(headers):
                        row.append("") 
                    dados.append(dict(zip(headers, row)))

      
        if not dados:
            return jsonify({'erro': 'Nenhum dado encontrado no CSV.'}), 404

        return jsonify({'dados': dados}), 200

    except requests.exceptions.RequestException as e:
        return jsonify({'erro': f'Erro ao acessar o CSV: {str(e)}'}), 500
    except Exception as e:
        return jsonify({'erro': f'Ocorreu um erro ao processar o CSV: {str(e)}'}), 500
    
## --------------------------------------------------------------------C O M E R C I A L I Z A Ç Ã O------------------------------------------------------------- ##

@main.route('/comercializacao')
@login_required
def comercializacao():
    return render_template('comercializacao.html', title='Processamento')

@main.route('/api/comercializacao', methods=['GET'])
@login_required
def api_comercializacao():
    """
    Endpoint para retornar os dados da tabela de comercializacao para o ano especificado.
    """
    ano = request.args.get('ano', '2023')  # Define 2023 como ano padrão
    try:
        data = fetch_comerci_data(ano)
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@main.route('/comercializacao/<int:ano>', methods=['GET'])
@login_required
def comercializacao_por_ano(ano):
    """
    Endpoint para buscar dados de produção de acordo com o ano.
    """
    try:
     
        url = f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao=opt_04"


        response = requests.get(url)
        response.raise_for_status()  

  
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table', {'class': 'tb_base tb_dados'})

     
        rows = []
        if table:
            for row in table.find_all('tr'):
                cols = [col.text.strip() for col in row.find_all('td')]
                if cols:
                    rows.append(cols)

    
        return jsonify({'ano': ano, 'dados': rows})

    except Exception as e:
        return jsonify({'erro': str(e)}), 500
    
@main.route('/comercializacao_csv', methods=['GET'])
@login_required
def comercializacao_csv():
    """
    Endpoint que baixa o CSV de comercializacao e retorna os dados em formato JSON.
    """
    csv_url = "http://vitibrasil.cnpuv.embrapa.br/download/Comercio.csv"
    

    try:
      
        response = requests.get(csv_url)
        response.raise_for_status()  

   
        decoded_content = response.content.decode('utf-8')
        csv_reader = csv.reader(io.StringIO(decoded_content), delimiter=';')

        dados = []
        headers = None
        for index, row in enumerate(csv_reader):
            if index == 0:
               
                headers = [header.strip() for header in row]
            else:
                
                if any(cell.strip() for cell in row):
                   
                    while len(row) < len(headers):
                        row.append("") 
                    dados.append(dict(zip(headers, row)))

      
        if not dados:
            return jsonify({'erro': 'Nenhum dado encontrado no CSV.'}), 404

        return jsonify({'dados': dados}), 200

    except requests.exceptions.RequestException as e:
        return jsonify({'erro': f'Erro ao acessar o CSV: {str(e)}'}), 500
    except Exception as e:
        return jsonify({'erro': f'Ocorreu um erro ao processar o CSV: {str(e)}'}), 500
    
## --------------------------------------------------------------------I M P O R T A Ç Ã O----------------------------------------------------------------------- ##

@main.route('/importacao')
@login_required
def importacao():
    return render_template('importacao.html', title='Importacao')

@main.route('/api/importacao', methods=['GET'])
@login_required
def importacao_por_ano_opcao():
    try:
        ano = request.args.get('ano', type=int)
        opcao = request.args.get('opcao', type=str)

        if not ano or not opcao:
            return jsonify({'erro': 'Parâmetros "ano" e "opcao" são obrigatórios.'}), 400

        url = f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao=opt_05&subopcao={opcao}"
        
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table', {'class': 'tb_base tb_dados'})

        rows = []
        if table:
            for row in table.find_all('tr'):
                cols = [col.text.strip() for col in row.find_all('td')]
                if cols:
                    rows.append(cols)

        return jsonify({'ano': ano, 'opcao': opcao, 'dados': rows})

    except requests.exceptions.RequestException as e:
        return jsonify({'erro': f'RequestException: {str(e)}'}), 500

    except Exception as e:
        return jsonify({'erro': f'Erro interno: {str(e)}'}), 500
    
@main.route('/importacao_csv', methods=['GET'])
@login_required
def importacao_csv():
    """
    Endpoint que baixa o CSV de importacao e retorna os dados em formato JSON.
    """
    csv_url = "http://vitibrasil.cnpuv.embrapa.br/download/ImpSuco.csv"

    try:
   
        response = requests.get(csv_url)
        response.raise_for_status()  

        decoded_content = response.content.decode('utf-8')
        csv_reader = csv.reader(io.StringIO(decoded_content), delimiter=';')

        dados = []
        headers = None
        for index, row in enumerate(csv_reader):
            if index == 0:
              
                headers = [header.strip() for header in row]
            else:
           
                if any(cell.strip() for cell in row):
                  
                    while len(row) < len(headers):
                        row.append("")  
                    dados.append(dict(zip(headers, row)))


        if not dados:
            return jsonify({'erro': 'Nenhum dado encontrado no CSV.'}), 404

        return jsonify({'dados': dados}), 200

    except requests.exceptions.RequestException as e:
        return jsonify({'erro': f'Erro ao acessar o CSV: {str(e)}'}), 500
    except Exception as e:
        return jsonify({'erro': f'Ocorreu um erro ao processar o CSV: {str(e)}'}), 500

## --------------------------------------------------------------------E X P O R T A Ç Ã O----------------------------------------------------------------------- ##

@main.route('/exportacao')
@login_required
def exportacao():
    return render_template('exportacao.html', title='exportacao')

@main.route('/api/exportacao', methods=['GET'])
@login_required
def exportacao_por_ano_opcao():
    try:
        ano = request.args.get('ano', type=int)
        opcao = request.args.get('opcao', type=str)

        if not ano or not opcao:
            return jsonify({'erro': 'Parâmetros "ano" e "opcao" são obrigatórios.'}), 400

        url = f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao=opt_06&subopcao={opcao}"
        
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table', {'class': 'tb_base tb_dados'})

        rows = []
        if table:
            for row in table.find_all('tr'):
                cols = [col.text.strip() for col in row.find_all('td')]
                if cols:
                    rows.append(cols)

        return jsonify({'ano': ano, 'opcao': opcao, 'dados': rows})

    except requests.exceptions.RequestException as e:
        return jsonify({'erro': f'RequestException: {str(e)}'}), 500

    except Exception as e:
        return jsonify({'erro': f'Erro interno: {str(e)}'}), 500
    
@main.route('/exportacao_csv', methods=['GET'])
@login_required
def exportacao_csv():
    """
    Endpoint que baixa o CSV de processamento e retorna os dados em formato JSON.
    """
    csv_url = "http://vitibrasil.cnpuv.embrapa.br/download/ExpSuco.csv"

    try:
    
        response = requests.get(csv_url)
        response.raise_for_status()  

     
        decoded_content = response.content.decode('utf-8')
        csv_reader = csv.reader(io.StringIO(decoded_content), delimiter=';')


        dados = []
        headers = None
        for index, row in enumerate(csv_reader):
            if index == 0:
              
                headers = [header.strip() for header in row]
            else:
             
                if any(cell.strip() for cell in row):
                  
                    while len(row) < len(headers):
                        row.append("")  
                    dados.append(dict(zip(headers, row)))

     
        if not dados:
            return jsonify({'erro': 'Nenhum dado encontrado no CSV.'}), 404

        return jsonify({'dados': dados}), 200

    except requests.exceptions.RequestException as e:
        return jsonify({'erro': f'Erro ao acessar o CSV: {str(e)}'}), 500
    except Exception as e:
        return jsonify({'erro': f'Ocorreu um erro ao processar o CSV: {str(e)}'}), 500