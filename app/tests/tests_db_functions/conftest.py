import pytest_asyncio
from app.tables import User
from app.tests.utils import TABLE_USER_1


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

#
# @pytest.fixture(scope="session")
# def event_loop():
#     policy = asyncio.get_event_loop_policy()
#     loop = policy.new_event_loop()
#     yield loop
#     loop.close()

