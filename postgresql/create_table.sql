CREATE SCHEMA estadisticas; 

DROP TABLE IF EXISTS estadisticas.poblacion_activa;
CREATE TABLE estadisticas.poblacion_activa
(
    id SERIAL PRIMARY KEY,
    sexo CHAR(7),
    formacion VARCHAR(150),
    total NUMERIC(10, 3),
    agno INT,
    periodo INT
)