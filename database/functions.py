from psycopg2 import connect, errors
import pandas as pd

from .configs import georeport_configs

def get_month_count():
    with connect(
            database=georeport_configs.DATABASE,
            user=georeport_configs.USER,
            password=georeport_configs.PASSWORD,
            host=georeport_configs.HOST,
            port=georeport_configs.PORT
    ) as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                f"SELECT * FROM get_count()"
            )
            df = pd.DataFrame(cursor.fetchall())
            df.rename(columns={0: 'Месяц', 1: 'Общее число протоколов'}, inplace=True)
            #df['Месяц'] = pd.to_datetime(df['Месяц'], format="%Y.%m")
            return df

def get_month_count_by_users():
    with connect(
            database=georeport_configs.DATABASE,
            user=georeport_configs.USER,
            password=georeport_configs.PASSWORD,
            host=georeport_configs.HOST,
            port=georeport_configs.PORT
    ) as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                f"SELECT * FROM get_users()"
            )
            users = [i[1] for i in cursor.fetchall()]
            df = get_month_count()

            for user in users:
                cursor.execute(
                    f"SELECT * FROM get_count_by_user('{user}')"
                )
                count = [i[1] for i in cursor.fetchall()]
                df[user] = count

            return df