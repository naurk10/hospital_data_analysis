import os
from sqlalchemy import create_engine
import pandas as pd

# Caminho absoluto para a pasta 'dados'
output_folder = r'C:\Users\super\Desktop\PROJETOS\hospital_data_analysis\dados'

# Criar a pasta 'dados' se ela não existir (usando os.makedirs apenas para garantir)
os.makedirs(output_folder, exist_ok=True)

# String de conexão com PostgreSQL via SQLAlchemy
engine = create_engine('postgresql+psycopg2://postgres:6463@localhost:5432/analise_hospitalar')

# Consulta SQL para pegar todos os dados da tabela 'pacientes'
query = "SELECT * FROM pacientes;"

# Usar o pandas para ler os dados diretamente do PostgreSQL
df = pd.read_sql(query, engine)

# Salvar os dados em um arquivo CSV na pasta 'dados'
df.to_csv(os.path.join(output_folder, 'pacientes.csv'), index=False)

print("Dados exportados para pacientes.csv com sucesso!")