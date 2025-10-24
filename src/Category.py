class Category:
    # корректные классовые счётчики
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        # создаём копию списка, чтобы избежать побочных эффектов
        self.__products = list(products) if products is not None else []
        # обновляем классовые счётчики
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product):
        self.__products.append(product)
        Category.product_count += 1

    def remove_product(self, product):
        if product in self.__products:
            self.__products.remove(product)
            Category.product_count -= 1
            return True
        return False

    @property
    def products(self):
        """Геттер для получения строкового представления товаров категории."""
        if not self.__products:
            return "Список товаров пуст"
        return "\n".join(
            f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            for product in self.__products
        )


def add_product(product):
    product.add_product(product)
