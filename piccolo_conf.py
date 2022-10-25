from piccolo.conf.apps import AppRegistry
from piccolo.engine.postgres import PostgresEngine

from dotenv import load_dotenv

import os

load_dotenv()

db_pass = os.getenv('POSTGRES_PASSWORD')

DB = PostgresEngine(config={
    'host': 'localhost',
    'database': 'flash-cards-chatbot',
    'user': 'postgres',
    'password': db_pass,
})


# A list of paths to piccolo apps
# e.g. ['blog.piccolo_app']
APP_REGISTRY = AppRegistry(apps=[])
