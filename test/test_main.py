from main.main import Category, Product


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
    # инициализация Category с продуктом обновляет счётчики
    Category.category_count = 0
    Category.product_count = 0

    p = Product("P", "d", 5.0, 1)
    c = Category("C", "desc", [p])
    assert c.name == "C"
    assert len(c.products) == 1
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
