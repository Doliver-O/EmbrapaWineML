# VitiML-API

**VitiML-API** é um projeto de análise de dados vitivinícolas da Embrapa, desenvolvido como parte de um curso de pós-graduação em Machine Learning. A API foi criada para consultar dados sobre vitivinicultura, como produção, processamento, comercialização, importação e exportação, com o objetivo de alimentar modelos de Machine Learning para análise preditiva e insights valiosos para o setor.

## Objetivo

Este projeto visa construir uma **Rest API** em Python que consulta os dados vitivinícolas fornecidos pela Embrapa, e serve como base para treinamento de modelos de Machine Learning para análise de dados agrícolas, previsões e otimização de processos relacionados ao setor vitivinícola.

### Funcionalidades

- Consulta pública de dados vitivinícolas da Embrapa.
- Acesso aos seguintes módulos de dados:
  - Produção
  - Processamento
  - Comercialização
  - Importação
  - Exportação
- API Documentada para fácil integração e uso por terceiros.
- Opção de autenticação via **JWT** (se implementada).
- MVP com deploy em ambiente de produção.

## Tecnologias Utilizadas

- **Python**: Linguagem principal para desenvolvimento da API.
- **Flask**: Framework web para construção da API Rest.
- **SQLAlchemy**: ORM para conexão com banco de dados.
- **JWT**: Autenticação (opcional).
- **PostgreSQL/MySQL**: Banco de dados para armazenamento dos dados consultados.
- **Docker**: Para containerização da aplicação (opcional, dependendo do plano de deploy).
- **Heroku/AWS**: Para deploy da API (plano de deploy sugerido).

## Instalação

Siga os passos abaixo para rodar a API localmente:

1. Clone o repositório:
    ```bash
    git clone https://github.com/SEU_USUARIO/VitiML-API.git
    cd VitiML-API
    ```

2. Crie e ative um ambiente virtual:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # No Windows use 'venv\Scripts\activate'
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Execute a API:
    ```bash
    python app.py
    ```

5. A API estará disponível em `http://localhost:5000`.

   ![Descrição da imagem](.app/static/imagem/front.png)

## Endpoints

### Autenticação
- **POST** `/login`: Autentica o usuário com `username` e `password`.
- **GET** `/login`: Exibe a página de login.

### Página Inicial
- **GET** `/`: Exibe a página inicial do site.

### Produção
- **GET** `/producao`: Exibe a página de produção.
- **GET** `/api/producao`: Retorna os dados da tabela de produção para o ano especificado.
- **GET** `/producao/<ano>`: Retorna dados de produção de acordo com o ano fornecido.
- **GET** `/producao_csv`: Faz o download do arquivo CSV de produção e retorna os dados em formato JSON.

### Processamento
- **GET** `/processamento`: Exibe a página de processamento.
- **GET** `/api/processamento`: Retorna dados de processamento para o ano e a opção especificados.
- **GET** `/processamento_csv`: Faz o download do arquivo CSV de processamento e retorna os dados em formato JSON.

### Comercialização
- **GET** `/comercializacao`: Exibe a página de comercialização.
- **GET** `/api/comercializacao`: Retorna os dados da tabela de comercialização para o ano especificado.
- **GET** `/comercializacao/<ano>`: Retorna dados de comercialização de acordo com o ano fornecido.

### Importação
- **GET** `/importacao`: Exibe a página de importação.
- **GET** `/api/importacao`: Retorna os dados de importação para o ano e a opção especificados.
- **GET** `/importacao_csv`: Faz o download do arquivo CSV de importação e retorna os dados em formato JSON.

### Exportação
- **GET** `/exportacao`: Exibe a página de exportação.
- **GET** `/api/exportacao`: Retorna os dados de exportação para o ano e a opção especificados.

## Tecnologias Utilizadas
- Python (Flask)
- JWT para autenticação
- Banco de Dados (SQLite/PostgreSQL)
- Documentação com Swagger

## Como Usar

1. **Autenticação:** Use o endpoint `/login` para autenticar com `username` e `password`.
2. **Consulta de Dados:** Utilize os endpoints de consulta para produção, processamento, comercialização, importação e exportação, especificando o ano ou opção desejada.
3. **Download de CSV:** Para obter dados em formato CSV, acesse os endpoints correspondentes com a opção `/csv`.
4. **API Response:** A API retorna os dados em formato JSON para facilitar a integração.

## Exemplos

**1. Consultar dados de produção para o ano de 2023:**
```http
GET /api/producao?ano=2023
