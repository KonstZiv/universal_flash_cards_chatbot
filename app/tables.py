from piccolo.table import Table
from piccolo.columns.column_types import UUID, Integer, Varchar, Text, Timestamp, ForeignKey


class User(Table, tablename="users"):
    id = UUID(primary_key=True)
    telegram_user_id = Integer(unique=True)
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
    context_class_id = ForeignKey(references=ContextClass)
    name = Varchar()
    name_alfa2 = Varchar()
    description = Text()


class UserContext(Table):
    id = UUID(primary_key=True)
    context_name_1 = ForeignKey(references=ContextName)
    context_name_2 = ForeignKey(references=ContextName)
    user_id = ForeignKey(references=User)
    last_date = Timestamp()


class Object(Table):
    autor_id = ForeignKey(references=User)
    context_name_id = ForeignKey(references=ContextName)
    text = Text()


class ObjectRelation(Table):
    autor_id = ForeignKey(references=User)
    context_name_1 = ForeignKey(references=Object)
    context_name_2 = ForeignKey(references=Object)


class Card(Table):
    id = UUID(primary_key=True)
    user_id = ForeignKey(references=User)
    object_relation_id = ForeignKey(references=ObjectRelation)
    box_number = Integer()
    last_date = Timestamp()
    repeats_amount = Integer()
    author = ForeignKey(references=User)
