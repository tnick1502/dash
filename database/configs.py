import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.split(__file__)[0], 'env.txt'))

class GeoreportConfigs:
    DATABASE = os.getenv('GEOREPORT_DATABASE')
    USER = os.getenv('GEOREPORT_USER')
    PASSWORD = os.getenv('GEOREPORT_PASSWORD')
    HOST = os.getenv('GEOREPORT_HOST')
    PORT = os.getenv('GEOREPORT_PORT')

georeport_configs = GeoreportConfigs()