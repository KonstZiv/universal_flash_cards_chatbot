from piccolo.conf.apps import AppRegistry
from piccolo.engine.postgres import PostgresEngine

from app.settings import settings


DB = PostgresEngine(config={
    'host': settings.POSTGRES_HOST,
    'database': settings.POSTGRES_DATABASE_NAME,
    'user': settings.POSTGRES_USER,
    'password': settings.POSTGRES_PASSWORD,
})

# A list of paths to piccolo apps
# e.g. ['blog.piccolo_app']
APP_REGISTRY = AppRegistry(apps=['bot_app.piccolo_app'])
