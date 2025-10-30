import pytest  # noqa: F401

from src.Products import Product
from src.Smartphone import Smartphone


def test_mixin_log_prints_on_creation(capfd):
    """
    Проверяет, что при создании объекта Product выводится сообщение в консоль.
    """
    _ = Product("Телефон", "Смартфон", 10000.0, 5)
    captured = capfd.readouterr()
    expected_output = "Product('Телефон', 'Смартфон', 10000.0, 5)\n"
    assert captured.out == expected_output


def test_mixin_log_for_smartphone(capfd):
    """
    Проверяет, что при создании объекта Smartphone также выводится сообщение.
    """
    _ = Smartphone(
        "Samsung Galaxy S23",
        "Флагманский смартфон",
        180000.0,
        3,
        98.5,
        "S23",
        512,
        "Чёрный",
    )
    captured = capfd.readouterr()
    expected_output = "Smartphone('Samsung Galaxy S23', 'Флагманский смартфон', 180000.0, 3, 98.5, 'S23', 512, 'Чёрный')\n"
    assert captured.out == expected_output


def test_mixin_log_repr_format():
    """
    Проверяет, что __repr__ возвращает правильную строку.
    """
    product = Product("Товар", "Описание", 500.0, 10)
    assert repr(product) == "Product('Товар', 'Описание', 500.0, 10)"


def test_mixin_log_with_new_product_method(capfd):
    """
    Проверяет, что метод new_product также вызывает логирование при создании.
    """
    data = {
        "name": "Ноутбук",
        "description": "Игровой ноутбук",
        "price": 95000.0,
        "quantity": 2,
    }
    _ = Product.new_product(data)
    captured = capfd.readouterr()
    expected_output = "Product('Ноутбук', 'Игровой ноутбук', 95000.0, 2)\n"
    assert captured.out == expected_output
