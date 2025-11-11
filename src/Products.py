from src.BaseProduct import BaseProduct
from src.MixinLog import MixinLog


class Product(MixinLog, BaseProduct):
    def __init__(self, name, description, price, quantity):
        if quantity <= 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

    @classmethod
    def new_product(cls, product_data):
        """
        Создаёт новый объект класса Product из словаря с данными о товаре.

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
        return self.__price

    @price.setter
    def price(self, value):
        """Сеттер для установки цены продукта с проверкой на корректность."""
        if value <= 0:
            print("Цена не должна быть нулевой или отрицательной")
        else:
            self.__price = value

    def __str__(self):
        """Возвращает строковое представление продукта."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Операция сложения продуктов."""
        if not isinstance(other, Product):
            raise TypeError("Нельзя складывать объекты разных типов")
        if type(self) is not type(other):
            raise TypeError("Можно складывать только товары одного и того же класса")
        return self.price * self.quantity + other.price * other.quantity
