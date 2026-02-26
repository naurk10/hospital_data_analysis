# Gerar relatorio.py

import pandas as pd
from sqlalchemy import create_engine
import os

# Conexão com o banco de dados com codificação UTF-8
engine = create_engine('postgresql+psycopg2://postgres:6463@localhost:5432/analise_hospitalar?client_encoding=UTF8')

# Consultas SQL para as análises
query_doencas = """
SELECT diagnostico, COUNT(*) AS total_internacoes
FROM internacoes
GROUP BY diagnostico
ORDER BY total_internacoes DESC;
"""

query_tempo_internacao = """
SELECT diagnostico, 
       AVG(data_alta - data_internacao) AS tempo_medio_internacao
FROM internacoes
GROUP BY diagnostico
ORDER BY tempo_medio_internacao DESC;
"""

query_volume_pacientes = """
SELECT DATE_TRUNC('month', data_internacao) AS mes, COUNT(*) AS volume_pacientes
FROM internacoes
GROUP BY mes
ORDER BY mes;
"""

# Carregar os dados das consultas no Pandas
df_doencas = pd.read_sql(query_doencas, engine)
df_tempo_internacao = pd.read_sql(query_tempo_internacao, engine)
df_volume_pacientes = pd.read_sql(query_volume_pacientes, engine)

# Verificar as colunas de cada DataFrame (para depuração)
print("Colunas de df_doencas:", df_doencas.columns)
print("Colunas de df_tempo_internacao:", df_tempo_internacao.columns)
print("Colunas de df_volume_pacientes:", df_volume_pacientes.columns)

# Garantir que não tenha fuso horário nas colunas de data, se necessário
def remove_timezone(df):
    for col in df.columns:
        if pd.api.types.is_datetime64_any_dtype(df[col]):  # Verifica se a coluna é de data
            df[col] = df[col].dt.tz_localize(None)  # Remove fuso horário
    return df

df_doencas = remove_timezone(df_doencas)
df_tempo_internacao = remove_timezone(df_tempo_internacao)
df_volume_pacientes = remove_timezone(df_volume_pacientes)

# Criar a pasta 'dados' se não existir
caminho_dados = r'C:\Users\super\Desktop\PROJETOS\hospital_data_analysis\dados'
if not os.path.exists(caminho_dados):
    os.makedirs(caminho_dados)

# Caminho para salvar os arquivos CSV com UTF-8 na pasta 'dados'
caminho_doencas = os.path.join(caminho_dados, 'doencas.csv')
caminho_tempo_internacao = os.path.join(caminho_dados, 'tempo_internacao.csv')
caminho_volume_pacientes = os.path.join(caminho_dados, 'volume_pacientes.csv')

# Salvar os dados em formato CSV com UTF-8-SIG (para garantir compatibilidade com Excel)
df_doencas.to_csv(caminho_doencas, encoding='utf-8-sig', index=False)
df_tempo_internacao.to_csv(caminho_tempo_internacao, encoding='utf-8-sig', index=False)
df_volume_pacientes.to_csv(caminho_volume_pacientes, encoding='utf-8-sig', index=False)

# Agora, converter os CSVs para Excel
caminho_excel = os.path.join(caminho_dados, 'relatorio_hospitalar.xlsx')

with pd.ExcelWriter(caminho_excel, engine='openpyxl') as writer:
    df_doencas.to_excel(writer, sheet_name='Doenças Frequentes', index=False)
    df_tempo_internacao.to_excel(writer, sheet_name='Tempo de Internação', index=False)
    df_volume_pacientes.to_excel(writer, sheet_name='Volume de Pacientes', index=False)

print("Relatório gerado com sucesso em:", caminho_excel)