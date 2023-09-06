"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


def test_calculate_total_price(item):
    assert Item.calculate_total_price(item) == 135


def test_apply_discount(item):
    Item.pay_rate = 0.8
    assert Item.apply_discount(item) == 36
