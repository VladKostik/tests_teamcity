import pytest
from .human import Human


@pytest.fixture
def human_1() -> Human:
    yield Human('Jah', 33, 'male')
