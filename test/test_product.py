import pytest

from src.Products import Product


def test_create_product_with_zero_quantity():
    """Тестируем, что создание товара с quantity=0 вызывает ValueError"""
    with pytest.raises(ValueError) as exc_info:
        Product("Трава", "Зелёная", 1000, 0)
    assert str(exc_info.value) == "Товар с нулевым количеством не может быть добавлен"


def test_create_product_with_negative_quantity():
    """Тестируем отрицательное количество"""
    with pytest.raises(ValueError) as exc_info:
        Product("Трава", "Зелёная", 1000, -5)
    assert str(exc_info.value) == "Товар с нулевым количеством не может быть добавлен"


def test_create_product_with_positive_quantity():
    """Тестируем нормальное создание товара"""
    product = Product("Телефон", "Смартфон", 50000, 10)
    assert product.name == "Телефон"
    assert product.quantity == 10
    assert product.price == 50000


def test_new_product_creates_correctly():
    """Тест метода new_product"""
    data = {"name": "Ноутбук", "description": "Игровой", "price": 80000, "quantity": 5}
    product = Product.new_product(data)
    assert product.name == "Ноутбук"
    assert product.quantity == 5


def test_new_product_with_zero_quantity():
    """Тест, что new_product тоже выбрасывает ошибку при quantity=0"""
    data = {
        "name": "Планшет",
        "description": "10 дюймов",
        "price": 30000,
        "quantity": 0,
    }
    with pytest.raises(ValueError) as exc_info:
        Product.new_product(data)
    assert str(exc_info.value) == "Товар с нулевым количеством не может быть добавлен"
