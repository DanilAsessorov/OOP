import pytest

from src.Category import Category
from src.LawnGrass import LawnGrass
from src.Products import Product
from src.Smartphone import Smartphone


def test_add_valid_products():
    category = Category("Тестовая категория", "Описание категории", [])
    smartphone = Smartphone(
        "Iphone 15", "Описание", 210000.0, 8, 98.2, "15", 512, "Gray space"
    )
    grass = LawnGrass(
        "Газонная трава", "Описание", 500.0, 20, "Россия", "7 дней", "Зеленый"
    )

    category.add_product(smartphone)
    category.add_product(grass)

    assert category.item_count == 2
    assert Category.product_count == 2


def test_add_invalid_product_type():
    category = Category("Категория", "Описание", [])
    basic_product = Product.new_product(
        {
            "name": "Базовый продукт",
            "description": "Описание",
            "price": 100.0,
            "quantity": 5,
        }
    )

    with pytest.raises(TypeError) as exc_info:
        category.add_product(basic_product)
    assert (
        str(exc_info.value)
        == "Можно добавлять только конкретные типы продуктов (Smartphone, LawnGrass и т.д.)"
    )


def test_add_non_product_object():
    category = Category("Категория", "Описание", [])

    with pytest.raises(TypeError) as exc_info:
        category.add_product("Это не продукт")
    assert (
        str(exc_info.value)
        == "Можно добавлять только объекты класса Product или его наследников"
    )


def test_remove_product():
    Category.category_count = 0
    Category.product_count = 0

    category = Category("Тестовая категория", "Описание категории", [])
    product = Smartphone(
        "Iphone 15", "Описание", 210000.0, 8, 98.2, "15", 512, "Gray space"
    )
    category.add_product(product)
    assert category.item_count == 1
    assert Category.product_count == 1

    category.remove_product(product)
    assert category.item_count == 0
    assert Category.product_count == 0


def test_str_representation():
    category = Category("Тестовая категория", "Описание", [])
    product = Smartphone(
        "Iphone 15", "Описание", 210000.0, 8, 98.2, "15", 512, "Gray space"
    )
    category.add_product(product)
    assert str(category) == "Тестовая категория, количество продуктов: 8 шт."


def test_products_property():
    category = Category("Тестовая категория", "Описание", [])
    product = Smartphone(
        "Iphone 15", "Описание", 210000.0, 8, 98.2, "15", 512, "Gray space"
    )
    category.add_product(product)
    assert "Iphone 15" in category.products


def test_get_average_price_empty_category():
    """Средняя цена в пустой категории должна быть 0 через try/except"""
    category = Category("Электроника", "Умные устройства")
    assert category.middle_price() == 0


def test_get_average_price_one_product():
    """Один товар — средняя цена равна его цене"""
    category = Category("Электроника", "Умные устройства")
    phone = Smartphone(
        "iPhone",
        "Смартфон",
        70000,
        5,
        efficiency="Высокая",
        model="13",
        memory="128",
        color="Чёрный",
    )
    category.add_product(phone)
    assert category.middle_price() == 70000


def test_get_average_price_multiple_products():
    grass1 = LawnGrass("Газон", "Зелёный", 1000, 10, "Россия", "14 дней", "Зелёный")
    grass2 = LawnGrass("Мох", "Теневой", 1500, 5, "Финляндия", "21 день", "Тёмный")
    category = Category("Сад", "Травы")
    category.add_product(grass1)  # ← добавляем оба
    category.add_product(grass2)
    assert category.middle_price() == (1000 + 1500) / 2


def test_get_average_price_with_subclasses():
    """Проверка, что средняя цена работает и для подклассов (Smartphone, LawnGrass)"""
    category = Category("Техника", "Гаджеты")
    phone = Smartphone("Galaxy", "Android", 60000, 3, "Высокая", "S23", "256", "Серый")
    tablet = Smartphone("iPad", "Apple", 40000, 2, "Средняя", "Air", "64", "Белый")
    category.add_product(phone)
    category.add_product(tablet)
    avg = category.middle_price()
    assert avg == (60000 + 40000) / 2  # = 50000.0
