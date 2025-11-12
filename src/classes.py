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

print("=== Начальное состояние счётчиков ===")
print(f"total_categories: {Category.total_categories}")
print(f"total_products: {Category.total_products}")

print("\n=== Создаём товары ===")
p1 = Product("Ноутбук", "Игровой", 79999.99, 10)
p2 = Product("Смартфон", "Android", 29999.0, 5)
p3 = Product("Планшет", "iOS", 39999.0, 3)
p4 = Product("Мышь", "Беспроводная", 0.0, 50)

print(f"Создано товаров: 4")

print("\n=== Создаём категории ===")
cat1 = Category("Электроника", "Электронные устройства", [p1, p2, p3])
print(f"Категория 1: {cat1.name} (товаров: {len(cat1.products)})")

cat2 = Category("Аксессуары", "Периферия", [p4])
print(f"Категория 2: {cat2.name} (товаров: {len(cat2.products)})")

cat3 = Category("Пустая категория", "Нет товаров", [])
print(f"Категория 3: {cat3.name} (товаров: {len(cat3.products)})")

print("\n=== Состояние счётчиков после создания категорий ===")
print(f"total_categories: {Category.total_categories}")  # Должно быть 3
print(f"total_products: {Category.total_products}")       # Должно быть 4 (3+1+0)

print("\n=== Детализация категорий ===")
print(f"Категория '{cat1.name}':")
for product in cat1.products:
    print(f"  - {product.name}: {product.price} руб. ({product.quantity} шт.)")

print(f"\nКатегория '{cat2.name}':")
for product in cat2.products:
    print(f"  - {product.name}: {product.price} руб. ({product.quantity} шт.)")

print(f"\nКатегория '{cat3.name}' содержит {len(cat3.products)} товаров.")