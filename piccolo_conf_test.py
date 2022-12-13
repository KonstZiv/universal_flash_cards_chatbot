from piccolo_conf import *

DB = PostgresEngine(
    config={
        "database": settings.POSTGRES_TEST_DATABASE_NAME
    }
)
