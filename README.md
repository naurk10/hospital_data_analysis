# Análise de Dados de Saúde (Hospital ou Clínica)

Este projeto realiza a análise de dados de saúde com foco em internações, tratamentos e diagnóstico dos pacientes. O objetivo é analisar dados como número de pacientes atendidos, categorias de doenças tratadas, tempo médio de internação, e identificar padrões de sazonalidade de doenças.

## Estrutura do Projeto

- **`scripts/`**: Contém scripts Python para se conectar ao banco de dados, rodar consultas SQL e gerar gráficos.
- **`dados/`**: Contém arquivos CSV gerados a partir dos dados do banco de dados.
- **`consultas_sql.py`**: Contém consultas SQL utilizadas para análise.
- **`notebooks/`**: Caso você utilize Jupyter, os notebooks podem ser armazenados aqui para análises interativas.

## Como Rodar

### Requisitos

- Python 3.x
- Bibliotecas: `pandas`, `sqlalchemy`, `psycopg2`, `matplotlib`
- Banco de dados PostgreSQL com o banco **`analise_hospitalar`** configurado.

### Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/hospital_data_analysis.git
