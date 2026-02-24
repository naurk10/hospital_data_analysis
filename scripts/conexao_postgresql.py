import os
from sqlalchemy import create_engine
import pandas as pd

# Criar a pasta 'dados' se ela não existir
os.makedirs('dados', exist_ok=True)

# String de conexão com PostgreSQL via SQLAlchemy
engine = create_engine('postgresql+psycopg2://postgres:6463@localhost:5432/analise_hospitalar')

# Consulta SQL para pegar todos os dados da tabela 'pacientes'
query = "SELECT * FROM pacientes;"

# Usar o pandas para ler os dados diretamente do PostgreSQL
df = pd.read_sql(query, engine)

# Salvar os dados em um arquivo CSV na pasta 'dados'
df.to_csv('dados/pacientes.csv', index=False)

print("Dados exportados para pacientes.csv com sucesso!")