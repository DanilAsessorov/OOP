from src.Products import Product

class Smartphone(Product):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        # Сначала создаём все атрибуты
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
        # Потом вызываем родительскую инициализацию
        super().__init__(name, description, price, quantity)

    def __repr__(self):
        """Полное строковое представление объекта Smartphone"""
        return (f"Smartphone({self.name!r}, {self.description!r}, {self.price!r}, {self.quantity!r}, "
                f"{self.efficiency!r}, {self.model!r}, {self.memory!r}, {self.color!r})")