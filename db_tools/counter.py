from psycopg2 import connect, errors
import datetime

from functions import user_ip
from configs import configs

'''
Пример использования:

@DBCounter("deviator")
def deviator():
    print("t")
'''

class DBCounter:
    param_name: str = None

    def __init__(self, param_name: str):
        self.param_name = param_name

    def __call__(self, f):
        def wrapper(*args, **kwargs):
            with connect(
                    database=configs.DATABASE,
                    user=configs.USER,
                    password=configs.PASSWORD,
                    host=configs.HOST,
                    port=configs.PORT
            ) as conn:
                try:
                    with conn.cursor() as cursor:
                        cursor.execute(
                            f"INSERT INTO statistic (user_ip, parameter_name, datetime) VALUES ({user_ip()}, {self.param_name}, {datetime.datetime.now()})"
                        )
                except errors as err:
                    print(err)
                    conn.rollback()
                finally:
                    f(*args, **kwargs)
        return wrapper
