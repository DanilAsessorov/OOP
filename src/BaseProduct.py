from abc import ABC, abstractmethod

class BaseProduct(ABC):
    """
    Абстрактный базовый класс для всех продуктов.
    Определяет обязательные методы, которые должны быть реализованы в наследниках.
    """

    @abstractmethod
    def __init__(self, description, name, price, quantity):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass
