from src.Products import Product


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = list(products) if products is not None else []
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product):
        """
        Добавляет продукт в категорию.
        Разрешено только для экземпляров класса Product или его подклассов.
        """
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product или его наследников")

        if product.__class__ == Product:
            raise TypeError("Можно добавлять только конкретные типы продуктов (Smartphone, LawnGrass и т.д.)")

        self.__products.append(product)
        Category.product_count += 1

    def remove_product(self, product):
        if product in self.__products:
            self.__products.remove(product)
            Category.product_count -= 1  # ⬅️ Обновляем общий счётчик
            return True
        return False

    @property
    def products(self):
        """Геттер для получения строкового представления товаров категории."""
        if not self.__products:
            return "Список товаров пуст"
        return "\n".join(str(product) for product in self.__products)

    @property
    def item_count(self):
        """Количество продуктов в категории."""
        return len(self.__products)

    def __str__(self):
        """Возвращает строковое представление категории в требуемом формате."""
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."
