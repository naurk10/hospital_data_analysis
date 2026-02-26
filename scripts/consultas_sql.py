-- consultas_sql.py

-- Volume de Pacientes por Mês
SELECT DATE_TRUNC('month', data_internacao) AS mes, COUNT(*) AS volume_pacientes
FROM internacoes
GROUP BY mes
ORDER BY mes;

-- Tempo Médio de Internação por Diagnóstico
SELECT diagnostico, 
       AVG(data_alta - data_internacao) AS tempo_medio_internacao
FROM internacoes
GROUP BY diagnostico
ORDER BY tempo_medio_internacao DESC;

-- Doenças Mais Frequentes
SELECT diagnostico, COUNT(*) AS total_internacoes
FROM internacoes
GROUP BY diagnostico
ORDER BY total_internacoes DESC;