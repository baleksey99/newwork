class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price  # Приватный атрибут цены
        self.quantity = quantity

    # Геттер для цены
    @property
    def price(self):
        return self.__price

    # Сеттер для цены с проверкой
    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value

    # Класс-метод для создания объекта Product из словаря
    @classmethod
    def new_product(cls, product_dict: dict):
        return cls(
            name=product_dict['name'],
            description=product_dict['description'],
            price=product_dict['price'],
            quantity=product_dict['quantity']
        )

    # Строковое представление объекта в нужном формате
    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."


class Category:
    # Атрибуты класса
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product] = None):
        self.name = name
        self.description = description
        self.__products = products if products is not None else []

        # Автоматическое увеличение счётчиков при создании объекта
        Category.category_count += 1
        Category.product_count += len(self.__products)

    @property
    def products(self):
        """
        Геттер: возвращает список отформатированных строк для каждого товара.
        Формат: "Название, цена руб. Остаток: X шт."
        Пример:
            ['Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.',
             'Iphone 15, 210000.0 руб. Остаток: 8 шт.']
        """
        return [str(product) for product in self.__products]

    @products.setter
    def products(self, value):
        if not isinstance(value, list):
            raise TypeError("products должен быть списком объектов Product")
        self.__products = value
        # Пересчитываем счётчик продуктов
        Category.product_count = sum(
            len(cat.__products)
            for cat in Category.__subclasses__() + [Category]
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
