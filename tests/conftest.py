import pytest

from src.item import Item


@pytest.fixture
def item():
    return Item("Молоко", 45, 3)
