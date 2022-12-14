from unittest import TestCase

from piccolo.conf.apps import Finder
from piccolo.table import create_db_tables_sync, drop_db_tables_sync

TABLES = Finder().get_table_classes()


class TestApp(TestCase):
    def setUp(self):
        create_db_tables_sync(*TABLES)

    def tearDown(self):
        drop_db_tables_sync(*TABLES)
