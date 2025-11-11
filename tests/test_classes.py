from src.main import Product, Category


def test_product_initialization():
    product = Product(
        name="Ноутбук",
        description="Игровой ноутбук",
        price=79999.99,
        quantity=10
    )
    assert product.name == "Ноутбук"
    assert product.description == "Игровой ноутбук"
    assert product.price == 79999.99
    assert product.quantity == 10


def test_product_price_can_be_zero():
    product = Product("Мышь", "Беспроводная", 0.0, 50)
    assert product.price == 0.0


def test_product_quantity_can_be_zero():
    product = Product("Клавиатура", "Механическая", 4999.50, 0)
    assert product.quantity == 0


def test_category_initialization():
    category = Category(
        name="Электроника",
        description="Электронные устройства",
        products=[]
    )
    assert category.name == "Электроника"
    assert category.description == "Электронные устройства"
    assert category.products == []


def test_category_with_products():
    p1 = Product("Смартфон", "Android", 29999.0, 5)
    p2 = Product("Планшет", "iOS", 39999.0, 3)
    category = Category("Мобильные устройства", "Смартфоны и планшеты", [p1, p2])
    assert len(category.products) == 2
    assert category.products[0].name == "Смартфон"
    assert category.products[1].name == "Планшет"


def test_total_categories_counter():
    # Очищаем счётчики перед тестом (если тесты запускаются многократно)
    Category.total_categories = 0
    Category.total_products = 0

    Category("Книги", "Художественная литература", [])
    Category("Одежда", "Повседневная одежда", [])

    assert Category.total_categories == 2


def test_total_products_counter():
    Category.total_categories = 0
    Category.total_products = 0

    p1 = Product("Книга 1", "Роман", 500.0, 10)
    p2 = Product("Книга 2", "Повесть", 400.0, 15)
    Category("Книги", "Художественная литература", [p1, p2])

    assert Category.total_products == 2  # 2 товара в категории

    p3 = Product("Футболка", "Хлопок", 1000.0, 20)
    Category("Одежда", "Повседневная одежда", [p3])

    assert Category.total_products == 3  # +1 товар во второй категории


def test_empty_category_does_not_add_to_total_products():
    Category.total_categories = 0
    Category.total_products = 0

    Category("Пустая", "Нет товаров", [])
    assert Category.total_categories == 1
    assert Category.total_products == 0  # товаров нет
