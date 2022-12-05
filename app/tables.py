import datetime

from piccolo.columns.column_types import (UUID, BigInt, ForeignKey, Integer,
                                          Text, Timestamp, Varchar)
from piccolo.table import Table


class User(Table, tablename="users"):
    id = UUID(primary_key=True)
    telegram_user_id = BigInt(unique=True)
    telegram_language = Varchar()
    user_name = Varchar()
    first_name = Varchar()
    last_name = Varchar()


class ContextClass(Table):
    id = UUID(primary_key=True)
    description = Text()
    name = Varchar()


class Context(Table):
    id = UUID(primary_key=True)
    context_class = ForeignKey(references=ContextClass)
    name = Varchar()
    name_alfa2 = Varchar()
    description = Text()


class UserContext(Table):
    id = UUID(primary_key=True)
    context_1 = ForeignKey(references=Context)
    context_2 = ForeignKey(references=Context)
    user = ForeignKey(references=User)
    last_date = Timestamp(default=datetime.datetime.now())


class Item(Table):
    author = ForeignKey(references=User)
    context = ForeignKey(references=Context)
    text = Text()


class ItemRelation(Table):
    author = ForeignKey(references=User)
    item_1 = ForeignKey(references=Item)
    item_2 = ForeignKey(references=Item)


class Card(Table):
    id = UUID(primary_key=True)
    user = ForeignKey(references=User)
    item_relation = ForeignKey(references=ItemRelation)
    box_number = Integer()
    last_date = Timestamp()
    repeats_amount = Integer()
    author = ForeignKey(references=User)
