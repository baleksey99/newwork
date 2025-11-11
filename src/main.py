class Product:
    """
    Класс, описывающий товар.
    """

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int
    ):
        """
        Инициализация экземпляра товара.

        :param name: название товара (строка)
        :param description: описание товара (строка)
        :param price: цена товара (число с плавающей точкой)
        :param quantity: количество в наличии (целое число)
        """
        self.name: str = name
        self.description: str = description
        self.price: float = price
        self.quantity: int = quantity

    def __repr__(self) -> str:
        return (f"Product(name='{self.name}', "
                f"price={self.price}, quantity={self.quantity})")

    def __str__(self) -> str:
        return f"{self.name} — {self.description} (Цена: {self.price} руб., в наличии: {self.quantity} шт.)"

class Category:
    """
    Класс, описывающий категорию товаров.
    """

    def __init__(
        self,
        name: str,
        description: str,
        products: list[Product] | None = None
    ):
        """
        Инициализация категории.

        :param name: название категории (строка)
        :param description: описание категории (строка)
        :param products: список товаров категории (список объектов Product, по умолчанию — пустой список)
        """
        self.name: str = name
        self.description: str = description
        self.products: list[Product] = products if products is not None else []

    def add_product(self, product: Product) -> None:
        """Добавить товар в категорию."""
        self.products.append(product)

    def remove_product(self, product_name: str) -> bool:
        """
        Удалить товар из категории по названию.

        :param product_name: название товара для удаления
        :return: True, если товар найден и удалён; False — если не найден
        """
        for i, product in enumerate(self.products):
            if product.name == product_name:
                del self.products[i]
                return True
        return False

    def get_product_by_name(self, name: str) -> Product | None:
        """
        Найти товар по названию.

        :param name: название товара
        :return: объект Product или None, если не найден
        """
        for product in self.products:
            if product.name == name:
                return product
        return None

    def __repr__(self) -> str:
        return (f!Category(name='{self.name}', "
                f!product_count={len(self.products)})")

    def __str__(self) -> str:
        products_str = "\n  ".join([str(p) for p in self.products]) if self.products else "Нет товаров"
        return (f"Категория: {self.name}\n"
                f"Описание: {self.description}\n"
                f"Товары:\n  {products_str}")