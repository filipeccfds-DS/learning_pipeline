Engenharia de Dados na Prática: Pipeline ETL de dados meteorológicos - Nível Iniciante

Requisitos e Configurações do Projeto
1. Pré-requisitos de Software (Ambiente Local)
Editor de Código: VS Code (recomendado com extensões Python e Docker).
Linguagem: Python 3.12 ou superior.
Banco de Dados: PostgreSQL 14+ rodando localmente (via Homebrew no Mac). 
Containerização: Docker Desktop para execução do ecossistema Airflow.
UV (Gerenciador de pacotes python) 
API Externa: Conta ativa no OpenWeatherMap com uma API Key gerada.

 Desenvolvimento Python (Scripts ETL)
O core do projeto será dividido em módulos para garantir a manutenção:
Extração: Script para requisição dos dados JSON da API OpenWeather.
Transformação: Utilização da biblioteca Pandas para limpeza, normalização e conversão de tipos
Carga: Implementação de conexão via SQLAlchemy e psycopg2 para ingestão dos dados no PostgreSQL

