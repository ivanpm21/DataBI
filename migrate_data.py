import pandas as pd
import psycopg as p

from db.db import DatabaseConnection
from db.credentials import get_credentials

dataframe = pd.read_csv('remote_work_productivity.csv', sep=',',thousands='.', decimal=',')

dataframe.drop('Employee_ID', axis=1, inplace=True)
dataframe.rename(columns={'Employment_Type': 'type', 'Hours_Worked_Per_Week': 'hours_worked_per_week',
                           'Productivity_Score': 'score', 'Well_Being_Score': 'satisfaction'}, inplace=True)
#dataframe[['agno', 'periodo']] = dataframe['Periodo'].str.split('T', n=1, expand=True)
#dataframe.drop(['Nacionalidad', 'Periodo'], axis=1, inplace=True)
#dataframe.rename(columns={'Sexo': 'sexo', 'Nivel de formacion alcanzado': 'formacion', 'Total': 'total'}, inplace=True)
#dataframe[["total", "agno", "periodo"]] = dataframe[["total", "agno", "periodo"]].apply(pd.to_numeric)


def _get_query() -> str:
    return '''
        INSERT INTO estadisticas.poblacion_activa (
            job_type,
            hours_worked_per_week,
            score,
            satisfaction
        )

        VALUES (%s, %s, %s, %s);
    '''

with DatabaseConnection(get_credentials()).df_cursor() as curr:
    curr.executemany(_get_query(), dataframe.to_numpy().tolist())