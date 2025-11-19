import pytest

from src.classes import Category, Product


# сброс счётчиков перед каждым тестом
@pytest.fixture(autouse=True)
def reset_category_counts():
    Category.category_count = 0
    Category.product_count = 0


# инициализация категории и подсчёт счётчиков
def test_category_init():
    category = Category("Электроника", "Товары для электроники")
    assert category.name == "Электроника"
    assert category.description == "Товары для электроники"
    assert len(category.products_list) == 0
    assert Category.category_count == 1
    assert Category.product_count == 0


# добавление товара в категорию (валидный случай)
def test_add_product():
    product = Product("Смартфон", "Современный смартфон", 30000, 10)
    category = Category("Электроника", "Товары для электроники")

    category.add_product(product)

    assert len(category.products_list) == 1
    assert Category.product_count == 1
    # Проверяем, что строковое представление товара есть в списке
    assert str(product) in category.products_list


# попытка добавить не-Product объект (проверка исключения)
def test_add_invalid_product():
    category = Category("Электроника", "Товары для электроники")
    with pytest.raises(TypeError, match="Можно добавлять только объекты класса Product"):
        category.add_product("Не товар")


# геттер products_list — формат вывода
def test_products_list_getter():
    product1 = Product("Ноутбук", "Мощный ноутбук", 70000, 5)
    product2 = Product("Мышь", "Эргономичная мышь", 1500, 20)
    category = Category("Компьютеры", "Компьютерная техника", [product1, product2])

    products_list = category.products_list
    assert len(products_list) == 2
    assert products_list[0] == "Ноутбук, 70000 руб. Остаток: 5 шт."
    assert products_list[1] == "Мышь, 1500 руб. Остаток: 20 шт."


# метод show_products — вывод в консоль
def test_show_products(capsys):
    product = Product("Клавиатура", "Механическая клавиатура", 5000, 15)
    category = Category("Периферия", "Устройства ввода", [product])

    category.show_products()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Клавиатура, 5000 руб. Остаток: 15 шт."


# создание категории с начальным списком товаров
def test_init_with_products():
    product = Product("Монитор", "27 дюймов", 25000, 8)
    category = Category("Мониторы", "Мониторы разных размеров", [product])

    assert len(category.products_list) == 1
    assert Category.product_count == 1
    assert str(product) in category.products_list


# проверка увеличения счётчиков при добавлении нескольких товаров
def test_multiple_products():
    category = Category("Аксессуары", "Аксессуары для гаджетов")
    product1 = Product("Чехол", "Силиконовый чехол", 500, 100)
    product2 = Product("Кабель", "USB-C кабель", 300, 50)

    category.add_product(product1)
    category.add_product(product2)

    assert len(category.products_list) == 2
    assert Category.product_count == 2


# проверка приватности атрибута __products (недоступен напрямую)
def test_private_products_attribute():
    category = Category("Книги", "Художественная литература")
    with pytest.raises(AttributeError):
        print(category.__products)
