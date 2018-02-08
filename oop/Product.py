class Product:

    def __init__(self, name, price):
        self._name = name
        self._price = price

    def get_price(self):
        return self._price


class DiscountProduct(Product):

    def __init__(self, name, price, disrate):
        super().__init__(name, price)
        self._disrate = disrate

    def get_price(self):
        return self._price - (self._price * self._disrate / 100)


p = Product("iPhone X", 80000)
dp = DiscountProduct('Google Pixel 2', 60000, 20)
print(p.get_price())
print(dp.get_price())