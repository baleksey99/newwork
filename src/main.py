class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity



class Category:
    # Атрибуты класса
    total_categories = 0
    total_products = 0

    def __init__(self, name: str, description: str, products: list[Product] = None):
        self.name = name
        self.description = description
        self.products = products if products is not None else []

        # Автоматическое увеличение счётчиков при создании объекта
        Category.total_categories += 1
        Category.total_products += len(self.products)