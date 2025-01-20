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

## Endpoints

### `/api/production`
- Método: `GET`
- Descrição: Retorna os dados sobre produção vitivinícola.
