import pytest
from src.classes import Category, Product


# Сброс счётчиков перед каждым тестом
@pytest.fixture(autouse=True)
def reset_category_counts():
    Category.category_count = 0
    Category.product_count = 0


# Инициализация категории и подсчёт счётчиков
def test_category_init():
    category = Category("Электроника", "Товары для электроники")
    assert category.name == "Электроника"
    assert category.description == "Товары для электроники"
    assert len(category.products) == 0  # Заменено: products_list → products
    assert Category.category_count == 1
    assert Category.product_count == 0


# Добавление товара в категорию (валидный случай)
def test_add_product():
    product = Product("Смартфон", "Современный смартфон", 30000, 10)
    category = Category("Электроника", "Товары для электроники")

    category.add_product(product)

    assert len(category.products) == 1  # Заменено: products_list → products
    assert Category.product_count == 1
    # Проверяем, что строковое представление товара есть в списке
    assert str(product) in category.products  # Заменено: products_list → products


# Попытка добавить не-Product объект (проверка исключения)
def test_add_invalid_product():
    category = Category("Электроника", "Товары для электроники")
    with pytest.raises(TypeError, match="Можно добавлять только объекты класса Product"):
        category.add_product("Не товар")


# Геттер products — формат вывода
def test_products_getter():
    product1 = Product("Ноутбук", "Мощный ноутбук", 70000, 5)
    product2 = Product("Мышь", "Эргономичная мышь", 1500, 20)
    category = Category("Компьютеры", "Компьютерная техника", [product1, product2])

    products = category.products  # Заменено: products_list → products
    assert len(products) == 2
    assert products[0] == "Ноутбук, 70000 руб. Остаток: 5 шт."
    assert products[1] == "Мышь, 1500 руб. Остаток: 20 шт."


# Метод show_products — вывод в консоль
def test_show_products(capsys):
    product = Product("Клавиатура", "Механическая клавиатура", 5000, 15)
    category = Category("Периферия", "Устройства ввода", [product])

    category.show_products()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Клавиатура, 5000 руб. Остаток: 15 шт."


# Создание категории с начальным списком товаров
def test_init_with_products():
    product = Product("Монитор", "27 дюймов", 25000, 8)
    category = Category("Мониторы", "Мониторы разных размеров", [product])

    assert len(category.products) == 1  # Заменено: products_list → products
    assert Category.product_count == 1
    assert str(product) in category.products  # Заменено: products_list → products


# Проверка увеличения счётчиков при добавлении нескольких товаров
def test_multiple_products():
    category = Category("Аксессуары", "Аксессуары для гаджетов")
    product1 = Product("Чехол", "Силиконовый чехол", 500, 100)
    product2 = Product("Кабель", "USB-C кабель", 300, 50)

    category.add_product(product1)
    category.add_product(product2)

    assert len(category.products) == 2
    assert Category.product_count == 2


# Проверка приватности атрибута __products
def test_private_products_attribute():
    category = Category("Книги", "Художественная литература")
    with pytest.raises(AttributeError):
        print(category.__products)


# Тест строкового представления Product
def test_product_str():
    product = Product("Смартфон", "Современный смартфон", 30000, 10)
    assert str(product) == "Смартфон, 30000 руб. Остаток: 10 шт."


# Тест строкового представления Category
def test_category_str():
    product1 = Product("Ноутбук", "Мощный ноутбук", 70000, 5)
    product2 = Product("Мышь", "Эргономичная мышь", 1500, 20)
    category = Category("Компьютеры", "Компьютерная техника", [product1, product2])
    assert str(category) == "Компьютеры, количество продуктов: 2 шт."


# Тест сложения продуктов (a + b)
def test_product_addition():
    product1 = Product("Смартфон", "Современный смартфон", 100, 10)   # 100 × 10 = 1000
    product2 = Product("Наушники", "Беспроводные", 200, 2)              # 200 × 2 = 400
    result = product1 + product2
    assert result == 1400  # 1000 + 400


# Тест ошибки при сложении с не-Product
def test_product_addition_type_error():
    product = Product("Смартфон", "Современный смартфон", 100, 10)
    with pytest.raises(TypeError, match="Складывать можно только объекты класса Product"):
        product + "Не товар"
