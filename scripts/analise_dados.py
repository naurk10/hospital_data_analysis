# analise_dados.py

from sqlalchemy import create_engine
import pandas as pd
import matplotlib.pyplot as plt

# Configuração da conexão com o PostgreSQL
engine = create_engine('postgresql+psycopg2://postgres:6463@localhost:5432/analise_hospitalar')

# Consultas SQL para as análises

# 1. Doenças Mais Frequentes
query_doencas = """
SELECT diagnostico, COUNT(*) AS total_internacoes
FROM internacoes
GROUP BY diagnostico
ORDER BY total_internacoes DESC;
"""

# 2. Tempo Médio de Internação por Diagnóstico
query_tempo_internacao = """
SELECT diagnostico, 
       AVG(data_alta - data_internacao) AS tempo_medio_internacao
FROM internacoes
GROUP BY diagnostico
ORDER BY tempo_medio_internacao DESC;
"""

# 3. Volume de Pacientes por Mês
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

# Exibir os dados
print("Doenças Mais Frequentes:")
print(df_doencas)

print("\nTempo Médio de Internação por Diagnóstico:")
print(df_tempo_internacao)

print("\nVolume de Pacientes por Mês:")
print(df_volume_pacientes)

# **Gráficos**

# Gráfico para Doenças Mais Frequentes
df_doencas.plot(kind='bar', x='diagnostico', y='total_internacoes', title='Doenças Mais Frequentes')
plt.xlabel('Diagnóstico')
plt.ylabel('Total de Internações')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Gráfico para Tempo Médio de Internação por Diagnóstico
df_tempo_internacao.plot(kind='bar', x='diagnostico', y='tempo_medio_internacao', title='Tempo Médio de Internação por Diagnóstico')
plt.xlabel('Diagnóstico')
plt.ylabel('Tempo Médio de Internação (dias)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Gráfico para Volume de Pacientes por Mês
df_volume_pacientes.plot(kind='line', x='mes', y='volume_pacientes', title='Volume de Pacientes por Mês')
plt.xlabel('Mês')
plt.ylabel('Volume de Pacientes')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()