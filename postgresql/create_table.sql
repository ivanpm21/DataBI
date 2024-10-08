CREATE SCHEMA estadisticas; 

DROP TABLE IF EXISTS estadisticas.poblacion_activa;
CREATE TABLE estadisticas.poblacion_activa
(
    job_type    VARCHAR(10),
    hours_worked_per_week INT,
    score INT,
    satisfaction INT
)

