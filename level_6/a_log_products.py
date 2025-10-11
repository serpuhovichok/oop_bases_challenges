"""
У нас есть различные типы классы для различных типов продуктов. Но мы ничего не знаем о том что происходит, когда мы вызываем
эти методы, хотелось бы простейшего логирования

Задания:
    1. Создайте класс PrintLoggerMixin и метод log у него, который будет принтить переданное в него сообщение.
    2. Используйте этот миксин, чтобы залогировать все методы у PremiumProduct и DiscountedProduct.
       Добавьте миксин и используйте новый метод во всех методах основных классов.
    3. Вызовите у экземпляров PremiumProduct и DiscountedProduct все возможные методы и убедитесь, что вызовы логируются.
"""


class PrintLoggerMixin:
    def log(self, message: str) -> None:
        print(message)


class Product:
    def __init__(self, title: str, price: float):
        self.title = title
        self.price = price

    def get_info(self):
        return f'Product {self.title} with price {self.price}'


class PremiumProduct(Product, PrintLoggerMixin):
    def increase_price(self):
        self.price *= 1.2
        self.log(f"Price increased. New price {self.price}")

    def get_info(self):
        base_info = super().get_info()
        result = f'{base_info} (Premium)'
        self.log(f"Info received: {result}")
        return result


class DiscountedProduct(Product, PrintLoggerMixin):
    def decrease_price(self):
        self.price /= 1.2
        self.log(f"Price decreased. New price {self.price}")

    def get_info(self):
        base_info = super().get_info()
        result = f'{base_info} (Discounted)'
        self.log(f"Info received: {result}")
        return result

if __name__ == '__main__':
    product_1 = PremiumProduct(title="Premium product", price=100.)
    product_1.increase_price()
    product_1.get_info()
    product_2 = DiscountedProduct(title="Discounted product", price=10.)
    product_2.decrease_price()
    product_2.get_info()
