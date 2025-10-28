from main import Category, Product


def test_product_init():
    # простой тест инициализации Product
    Category.category_count = 0
    Category.product_count = 0

    p = Product("P", "d", 10.0, 1)
    assert p.name == "P"
    assert p.description == "d"
    assert p.price == 10.0
    assert p.quantity == 1


def test_category_init_and_counts():
    Category.category_count = 0
    Category.product_count = 0

    p = Product("P", "d", 5.0, 1)
    c = Category("C", "desc", [p])
    assert c.name == "C"
    assert c.item_count == 1
    assert Category.category_count == 1
    assert Category.product_count == 1


def test_add_and_remove_product_updates_count():
    # простая проверка add/remove
    Category.category_count = 0
    Category.product_count = 0

    p = Product("P", "d", 2.0, 1)
    c = Category("C", "", [])
    c.add_product(p)
    assert Category.product_count == 1
    c.remove_product(p)
    assert Category.product_count == 0


def test_category_count_increment():
    # проверка увеличения количества категорий
    Category.category_count = 0
    Category.product_count = 0

    Category("A", "", [])
    Category("B", "", [])
    assert Category.category_count == 2


def test_product_price_property():
    # проверка геттера и сеттера цены
    p = Product("P", "d", 10.0, 1)
    assert p.price == 10.0

    p.price = 15.0  # Устанавливаем новую цену через сеттер
    assert p.price == 15.0

    p.price = -5  # пытаемся установить отрицательную цену
    assert p.price == 15.0  # цена не должна измениться


def test_product_new_product():
    product_data = {
        "name": "Смартфон",
        "description": "Высококачественный смартфон",
        "price": 25000.0,
        "quantity": 10,
    }

    product = Product.new_product(product_data)

    assert product.name == "Смартфон"
    assert product.description == "Высококачественный смартфон"
    assert product.price == 25000
    assert product.quantity == 10


def test_category_product_property():
    # проверка геттера products в виде строкового представления
    p1 = Product("Пылесос", "Мощный пылесос", 15000.0, 5)
    p2 = Product("Утюг", "Гладильное устройство", 3000.0, 8)
    category = Category("Электроника", "Категория бытовой техники", [p1, p2])

    expected_output = (
        "Пылесос, 15000.0 руб. Остаток: 5 шт.\n" "Утюг, 3000.0 руб. Остаток: 8 шт."
    )
    assert category.products == expected_output


def test_product_str():
    p = Product("Samsung Galaxy S23", "256GB, Серый цвет", 180000.0, 5)
    assert str(p) == "Samsung Galaxy S23, 180000.0 руб. Остаток: 5 шт."


def test_category_str():
    p1 = Product("Samsung Galaxy S23", "256GB, Серый цвет", 180000.0, 5)
    p2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    c = Category("Смартфоны", "Описание", [p1, p2])
    assert str(c) == "Смартфоны, количество продуктов: 13 шт."  # 5 + 8


def test_product_addition():
    p1 = Product("Samsung Galaxy S23", "256GB, Серый цвет", 180000.0, 5)
    p2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)

    result = p1 + p2
    assert result == 180000.0 * 5 + 210000.0 * 8  # 900000 + 1680000 = 2580000


def test_category_products_property():
    p1 = Product("Samsung Galaxy S23", "256GB, Серый цвет", 180000.0, 5)
    p2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    c = Category("Смартфоны", "Описание", [p1, p2])

    expected = (
        "Samsung Galaxy S23, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт."
    )
    assert c.products == expected
