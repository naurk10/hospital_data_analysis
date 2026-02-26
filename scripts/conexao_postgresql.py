# conexao_postgresql.py
import psycopg2
import pandas as pd

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="analise_hospitalar_restore",
    user="postgres",
    password="6463"
)
conn.set_client_encoding("UTF8")

import pandas as pd

check = pd.read_sql("SHOW client_encoding;", con=conn)
print(check)

query = "SELECT * FROM pacientes LIMIT 5;"
df = pd.read_sql(query, con=conn)

import sys
print("stdout encoding:", sys.stdout.encoding)
print("teste:", "João")

print(df)

conn.close()