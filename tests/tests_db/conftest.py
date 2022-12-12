import asyncio

import pytest
import pytest_asyncio

from typing import Any, Optional



from app.tables import Context, User, UserContext
from tests.tests_db.utils import TABLE_USER_1


@pytest_asyncio.fixture(scope="session")
async def save_table_user() -> User:
    await User.delete(force=True)
    try:
        yield await TABLE_USER_1.save()
    finally:
        await User.delete(force=True)


def setup():
    pass


def teardown(params):
    pass


@pytest_asyncio.fixture(scope="session")
def setup_teardown(params):
    setup(params)
    yield
    teardown(params)
