import os
import pandas as pd
import matplotlib.pyplot as plt
import psycopg2

DB_NAME = "analise_hospitalar"
DB_USER = "postgres"
DB_PASS = "6463"
DB_HOST = "localhost"
DB_PORT = 5432


def get_conn():
    conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )
    conn.set_client_encoding("UTF8")
    return conn


def ensure_docs_dir():
    os.makedirs("docs", exist_ok=True)


def save_plot(path: str):
    plt.tight_layout()
    plt.savefig(path, dpi=200)
    plt.close()


def grafico_internacoes_por_mes(conn):
    query = """
    SELECT DATE_TRUNC('month', data_internacao)::date AS mes,
           COUNT(*) AS total
    FROM internacoes
    WHERE data_internacao IS NOT NULL
    GROUP BY 1
    ORDER BY 1;
    """
    df = pd.read_sql(query, conn)
    if df.empty:
        return

    plt.figure()
    plt.plot(df["mes"], df["total"], marker="o")
    plt.title("Internacoes por mes")
    plt.xlabel("Mes")
    plt.ylabel("Total")
    plt.xticks(rotation=45)
    save_plot("docs/grafico_internacoes_mes.png")


def grafico_top_diagnosticos(conn):
    query = """
    SELECT diagnostico,
           COUNT(*) AS total
    FROM internacoes
    WHERE diagnostico IS NOT NULL
      AND diagnostico <> ''
    GROUP BY 1
    ORDER BY 2 DESC
    LIMIT 10;
    """
    df = pd.read_sql(query, conn)
    if df.empty:
        return

    plt.figure()
    plt.bar(df["diagnostico"], df["total"])
    plt.title("Top 10 diagnosticos de internacao")
    plt.xlabel("Diagnostico")
    plt.ylabel("Total")
    plt.xticks(rotation=45, ha="right")
    save_plot("docs/grafico_top_diagnosticos.png")


def grafico_genero(conn):
    query = """
    SELECT genero,
           COUNT(*) AS total
    FROM pacientes
    WHERE genero IS NOT NULL
      AND genero <> ''
    GROUP BY 1
    ORDER BY 2 DESC;
    """
    df = pd.read_sql(query, conn)
    if df.empty:
        return

    plt.figure()
    plt.bar(df["genero"], df["total"])
    plt.title("Distribuicao de pacientes por genero")
    plt.xlabel("Genero")
    plt.ylabel("Total")
    save_plot("docs/grafico_genero.png")


def grafico_tempo_medio_por_especialidade(conn):
    query = """
    SELECT
      e.nome_especialidade AS especialidade,
      AVG((i.data_alta - i.data_internacao))::numeric(10,2) AS dias_medio
    FROM internacoes i
    JOIN especialidades e ON e.id = i.especialidade_id
    WHERE i.data_internacao IS NOT NULL
      AND i.data_alta IS NOT NULL
      AND i.data_alta >= i.data_internacao
    GROUP BY 1
    ORDER BY 2 DESC;
    """
    df = pd.read_sql(query, conn)
    if df.empty:
        return

    plt.figure()
    plt.bar(df["especialidade"], df["dias_medio"])
    plt.title("Tempo medio de permanencia por especialidade (dias)")
    plt.xlabel("Especialidade")
    plt.ylabel("Dias (media)")
    plt.xticks(rotation=45, ha="right")
    save_plot("docs/grafico_tempo_medio_especialidade.png")


def main():
    ensure_docs_dir()
    conn = get_conn()
    try:
        grafico_internacoes_por_mes(conn)
        grafico_top_diagnosticos(conn)
        grafico_genero(conn)
        grafico_tempo_medio_por_especialidade(conn)
        print("OK: graficos gerados em /docs")
    finally:
        conn.close()


if __name__ == "__main__":
    main()