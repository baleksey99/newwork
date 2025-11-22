import pytest
from src.classes import Category, Product
from src.classes import Smartphone, LawnGrass


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

# Тест создания Smartphone
def test_smartphone_creation():
    smartphone = Smartphone(
        name="Samsung S23",
        description="Флагман 2023",
        price=100000,
        quantity=5,
        efficiency=95.5,
        model="S23",
        memory=256,
        color="Чёрный"
    )
    assert smartphone.name == "Samsung S23"
    assert smartphone.efficiency == 95.5
    assert smartphone.model == "S23"
    assert smartphone.memory == 256
    assert smartphone.color == "Чёрный"


# Тест создания LawnGrass
def test_lawn_grass_creation():
    grass = LawnGrass(
        name="Газонная трава",
        description="Элитная трава",
        price=500,
        quantity=20,
        country="Россия",
        germination_period="7 дней",
        color="Зелёный"
    )
    assert grass.name == "Газонная трава"
    assert grass.country == "Россия"
    assert grass.germination_period == "7 дней"
    assert grass.color == "Зелёный"


# Тест сложения смартфонов
def test_add_smartphones():
    smartphone1 = Smartphone("S23", "Флагман", 100000, 5, 95.5, "S23", 256, "Чёрный")
    smartphone2 = Smartphone("iPhone 15", "Флагман", 120000, 3, 98.0, "15", 512, "Белый")
    result = smartphone1 + smartphone2
    assert result == 100000 * 5 + 120000 * 3  # 500000 + 360000 = 860000


# Тест сложения газонных трав
def test_add_lawn_grass():
    grass1 = LawnGrass("Трава 1", "Описание", 500, 20, "Россия", "7 дней", "Зелёный")
    grass2 = LawnGrass("Трава 2", "Описание", 400, 15, "США", "5 дней", "Тёмно‑зелёный")
    result = grass1 + grass2
    assert result == 500 * 20 + 400 * 15  # 10000 + 6000 = 16000


# Тест ошибки при сложении разных классов
def test_add_different_types():
    smartphone = Smartphone("S23", "Флагман", 100000, 5, 95.5, "S23", 256, "Чёрный")
    grass = LawnGrass("Трава", "Описание", 500, 20, "Россия", "7 дней", "Зелёный")
    with pytest.raises(TypeError, match="Нельзя складывать Smartphone и LawnGrass"):
        smartphone + grass

# Тест добавления смартфона в категорию
def test_add_smartphone_to_category():
    smartphone = Smartphone("S23", "Флагман", 100000, 5, 95.5, "S23", 256, "Чёрный")
    category = Category("Смартфоны", "Мобильные устройства")
    category.add_product(smartphone)
    assert len(category.products) == 1
    assert Category.product_count == 1

# Тест добавления газонной травы в категорию
def test_add_lawn_grass_to_category():
    grass = LawnGrass("Трава", "Описание", 500, 20, "Россия", "7 дней", "Зелёный")
    category = Category("Газонная трава", "Семена")
    category.add_product(grass)
    assert len(category.products) == 1
    assert Category.product_count == 1
