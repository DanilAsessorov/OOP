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
    basic_product = Product.new_product({
        "name": "Базовый продукт",
        "description": "Описание",
        "price": 100.0,
        "quantity": 5
    })

    with pytest.raises(TypeError) as exc_info:
        category.add_product(basic_product)
    assert str(exc_info.value) == "Можно добавлять только конкретные типы продуктов (Smartphone, LawnGrass и т.д.)"


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