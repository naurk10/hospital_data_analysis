# Análise de Dados Hospitalares

Este projeto realiza a análise de dados hospitalares, incluindo informações sobre pacientes, internações, tratamentos e doenças. O objetivo é entender as características e os padrões dos pacientes, como a duração das internações, os tratamentos aplicados e as doenças mais comuns.

## Estrutura do Projeto

- **`consultas.sql`**: Contém todas as consultas SQL usadas para análise dos dados.
- **`scripts/conexao_postgresql.py`**: Script Python para se conectar ao banco de dados e executar as consultas SQL.
- **`dados/pacientes.csv`**: Arquivo CSV contendo os dados de pacientes extraídos do banco de dados PostgreSQL.

## Como Rodar

### Pré-requisitos

- Python 3.x
- Bibliotecas: `pandas`, `sqlalchemy`, `psycopg2`
- Banco de dados PostgreSQL com o banco de dados **`analise_hospitalar`** configurado.

### Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/hospital_data_analysis.git
