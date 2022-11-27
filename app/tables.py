import datetime

from piccolo.table import Table
from piccolo.columns.column_types import UUID, Integer, Varchar, Text, Timestamp, ForeignKey, BigInt


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


class ContextName(Table):
    id = UUID(primary_key=True)
    context_class = ForeignKey(references=ContextClass)
    name = Varchar()
    name_alfa2 = Varchar()
    description = Text()


class UserContext(Table):
    id = UUID(primary_key=True)
    context_1 = ForeignKey(references=ContextName)
    context_2 = ForeignKey(references=ContextName)
    user = ForeignKey(references=User)
    last_date = Timestamp(auto_update=datetime.datetime.now)


class Object(Table):
    autor = ForeignKey(references=User)
    context = ForeignKey(references=ContextName)
    text = Text()


class ObjectRelation(Table):
    autor = ForeignKey(references=User)
    context_1 = ForeignKey(references=Object)
    context_2 = ForeignKey(references=Object)


class Card(Table):
    id = UUID(primary_key=True)
    user = ForeignKey(references=User)
    object_relation = ForeignKey(references=ObjectRelation)
    box_number = Integer()
    last_date = Timestamp()
    repeats_amount = Integer()
    author = ForeignKey(references=User)
