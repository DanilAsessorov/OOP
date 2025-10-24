class Product:
    """класс данных о продукте"""

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_data):
        """
        Создаём новый обьект класса Product из словаря с данными о товаре.
        :param product_data: Словарь с ключами 'name', 'description', 'price', 'quantity'
        :return: Объект класса Product
        """
        return cls(
            product_data["name"],
            product_data["description"],
            product_data["price"],
            product_data["quantity"],
        )

    @property
    def price(self):
        """Геттер для получения цены продукта."""
        return self.price

    @price.setter
    def price(self, value):
        """Сеттер для установки цены продукта с проверкой на корректность."""
        if value < 0:
            print("Цена не может быть отрицательной")
        else:
            self.__price = value
