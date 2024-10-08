import pandas as pd

from db.database_conn import DatabaseConnection
from db.credentials import get_credentials

# Read data file
dataframe = pd.read_csv('../data/remote_work_productivity.csv', sep=',')

# Drop unused columns and renamed others for better access
dataframe.drop('Employee_ID', axis=1, inplace=True)
dataframe.rename(columns={'Employment_Type': 'type', 'Hours_Worked_Per_Week': 'hours_worked_per_week',
                           'Productivity_Score': 'score', 'Well_Being_Score': 'satisfaction'}, inplace=True)

# Define insertion query
def _get_query() -> str:
    return '''
        INSERT INTO stadistics.employees (
            job_type,
            hours_worked_per_week,
            score,
            satisfaction
        )

        VALUES (%s, %s, %s, %s);
    '''

# Connection with database and query execution
with DatabaseConnection(get_credentials()).df_cursor() as curr:
    curr.executemany(_get_query(), dataframe.to_numpy().tolist())