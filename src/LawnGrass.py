from src.Products import Product

class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        # Сначала создаём все атрибуты
        self.country = country
        self.germination_period = germination_period
        self.color = color
        # Потом вызываем родительскую инициализацию
        super().__init__(name, description, price, quantity)

    def __repr__(self):
        """Полное строковое представление объекта LawnGrass"""
        return (f"LawnGrass({self.name!r}, {self.description!r}, {self.price!r}, {self.quantity!r}, "
                f"{self.country!r}, {self.germination_period!r}, {self.color!r})")
