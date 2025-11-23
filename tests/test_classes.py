import pytest
from io import StringIO
import sys

from src.classes import (
    BaseProduct,
    CreationLogger,
    Product,
    Smartphone,
    LawnGrass,
    Category
)



def capture_output(func, *args, **kwargs):
    captured = StringIO()
    sys.stdout = captured
    try:
        result = func(*args, **kwargs)
    finally:
        sys.stdout = sys.__stdout__
    return captured.getvalue(), result



# Тесты для BaseProduct
def test_base_product_abstract():
    with pytest.raises(TypeError):
        BaseProduct("Тест", "Описание", 100.0, 5)



def test_creation_logger_prints_on_init(capsys):
    class TestClass(CreationLogger):
        def __init__(self, x, y):
            super().__init__(x, y)
            self.x = x
            self.y = y

    obj = TestClass(10, y=20)
    captured = capsys.readouterr()
    assert "TestClass(10, 20)" in captured.out

def test_creation_logger_works_with_product(capsys):
    product = Product("Продукт1", "Описание", 1200.0, 10)
    captured = capsys.readouterr()
    expected = "Product('Продукт1', 'Описание', 1200.0, 10)"
    assert expected in captured.out



def test_product_init():
    """Инициализация Product."""
    product = Product("Тест", "Описание теста", 100.0, 5)
    assert product.name == "Тест"
    assert product.description == "Описание теста"
    assert product.price == 100.0
    assert product.quantity == 5


def test_product_price_setter_valid():
    """Сеттер цены: корректное значение."""
    product = Product("Тест", "Описание", 100.0, 5)
    product.price = 150.0
    assert product.price == 150.0

def test_product_price_setter_invalid(capsys):
    """Сеттер цены: отрицательное — ошибка."""
    product = Product("Тест", "Описание", 100.0, 5)
    product.price = -50.0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == 100.0

def test_product_str():
    """Строковое представление Product."""
    product = Product("Смартфон", "Флагман", 50000.0, 3)
    assert str(product) == "Смартфон, 50000.0 руб. Остаток: 3 шт."

def test_product_addition():
    """Сложение двух Product: цена × количество."""
    p1 = Product("Товар1", "Первый", 100.0, 2)  # 200
    p2 = Product("Товар2", "Второй", 150.0, 3)  # 450
    assert p1 + p2 == 650.0

def test_product_addition_type_error():
    """Ошибка при сложении с не‑Product."""
    p = Product("Тест", "Описание", 100.0, 5)
    with pytest.raises(TypeError, match="Складывать можно только объекты класса Product"):
        p + "не продукт"

def test_product_addition_different_types():
    """Ошибка при сложении разных подклассов."""
    smartphone = Smartphone(
        name="S23",
        description="Флагман",
        price=100000.0,
        quantity=5,
        efficiency=95.5,
        model="S23",
        memory=256,
        color="Чёрный"
    )
    grass = LawnGrass(
        name="Трава",
        description="Зелёная",
        price=500.0,
        quantity=20,
        country="Россия",
        germination_period="7 дней",
        color="Зелёный"
    )
    with pytest.raises(TypeError, match="Нельзя складывать Smartphone и LawnGrass"):
        smartphone + grass

def test_product_new_product_from_dict():
    """Создание Product из словаря."""
    data = {
        "name": "Ноутбук",
        "description": "Игровой",
        "price": 80000.0,
        "quantity": 4
    }
    product = Product.new_product(data)
    assert product.name == "Ноутбук"
    assert product.price == 80000.0
    assert product.quantity == 4