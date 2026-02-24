from sqlalchemy import create_engine
import pandas as pd

# String de conexão com PostgreSQL via SQLAlchemy
engine = create_engine('postgresql+psycopg2://postgres:6463@localhost:5432/analise_hospitalar')

# Dados para inserir
data = {
    'nome': ['João Silva', 'Maria Souza'],
    'data_nascimento': ['1980-01-01', '1990-05-15'],
    'genero': ['Masculino', 'Feminino'],
    'endereco': ['Rua A, 123', 'Rua B, 456']
}

# Criar DataFrame
df = pd.DataFrame(data)

# Inserir os dados na tabela `pacientes` usando append para não substituir a tabela
df.to_sql('pacientes', engine, if_exists='append', index=False)

# Verificar os dados inseridos
query = "SELECT * FROM pacientes LIMIT 5;"
df_resultado = pd.read_sql(query, engine)
print(df_resultado)