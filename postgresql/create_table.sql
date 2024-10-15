CREATE SCHEMA stadistics; 

DROP TABLE IF EXISTS stadistics.employees;
CREATE TABLE stadistics.employees
(
    job_type    VARCHAR(10),
    hours_worked_per_week INT,
    score INT,
    satisfaction INT
)

