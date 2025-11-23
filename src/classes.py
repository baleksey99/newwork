
from abc import ABC, abstractmethod



class BaseProduct(ABC):
    """Абстрактный базовый класс для всех продуктов."""

    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    @property
    @abstractmethod
    def price(self) -> float:
        pass

    @price.setter
    @abstractmethod
    def price(self, value: float):
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass



class CreationLogger:
    """Миксин для логирования создания объектов."""

    def __init__(self, *args, **kwargs):
        class_name = self.__class__.__name__
        args_str = ', '.join([repr(arg) for arg in args])
        kwargs_str = ', '.join([f"{k}={v!r}" for k, v in kwargs.items()])
        all_args = ', '.join([args_str, kwargs_str]) if kwargs_str else args_str
        print(f"{class_name}({all_args})")




class Product(CreationLogger, BaseProduct):
    """Основной класс продукта."""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        super().__init__(name, description, price, quantity)
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, value: float):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if not isinstance(other, Product):
            raise TypeError("Складывать можно только объекты класса Product")
        if type(self) != type(other):
            raise TypeError(f"Нельзя складывать {type(self).__name__} и {type(other).__name__}")
        return self.price * self.quantity + other.price * other.quantity

    @classmethod
    def new_product(cls, product_dict: dict):
        return cls(
            name=product_dict['name'],
            description=product_dict['description'],
            price=product_dict['price'],
            quantity=product_dict['quantity']
        )



class Smartphone(Product):
    """Класс для смартфонов."""

    def __init__(self, name: str, description: str, price: float, quantity: int,
                 efficiency: float, model: str, memory: int, color: str):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color



class LawnGrass(Product):
    """Класс для газонной травы."""

    def __init__(self, name: str, description: str, price: float, quantity: int,
                 country: str, germination_period: str, color: str):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color



class Category:
    """Класс для категории товаров."""

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product] = None):
        self.name = name
        self.description = description
        self.__products = products if products is not None else []
        Category.category_count += 1
        Category.product_count += len(self.__products)

    @property
    def products(self) -> list[str]:
        return [str(product) for product in self.__products]

    @products.setter
    def products(self, value: list[Product]):
        if not isinstance(value, list):
            raise TypeError("products должен быть списком объектов Product")
        self.__products = value
        Category.product_count = sum(
            len(cat.__products) for cat in Category.__subclasses__() + [Category]
        )

    def add_product(self, product: Product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError("Можно добавлять только объекты класса Product")

    def show_products(self):
        for product in self.__products:
            print(product)

    def __str__(self) -> str:
        return f"{self.name}, количество продуктов: {Category.product_count} шт."