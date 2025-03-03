class Product:
    def __init__(self, name: str, price: float, quantity: int = 1):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} ({self.quantity} x {self.price:.2f} PLN)"

    def __repr__(self):
        return f"Product({self.name}, {self.price}, {self.quantity})"

    def __float__(self):
        return self.price * self.quantity

    def __int__(self):
        return int(self.__float__())


class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_product(self, product: Product):
        if product.name in self.items:
            self.items[product.name].quantity += product.quantity
        else:
            self.items[product.name] = product

    def __len__(self):
        return sum(product.quantity for product in self.items.values())

    def __getitem__(self, item):
        return self.items[item]

    def __setitem__(self, key, value: Product):
        self.items[key] = value

    def __delitem__(self, key):
        if key in self.items:
            del self.items[key]

    def __contains__(self, item):
        return item in self.items

    def __iter__(self):
        return iter(self.items.values())

    def __str__(self):
        return "\n".join(str(product) for product in self.items.values())

    def __repr__(self):
        return f"ShoppingCart({list(self.items.values())})"

    def __float__(self):
        return sum(float(product) for product in self.items.values())

    def __int__(self):
        return int(float(self))

    def __add__(self, other):
        if isinstance(other, ShoppingCart):
            new_cart = ShoppingCart()
            for product in self:
                new_cart.add_product(product)
            for product in other:
                new_cart.add_product(product)
            return new_cart
        raise TypeError("Can only add another ShoppingCart instance.")

    def __sub__(self, other):
        if isinstance(other, ShoppingCart):
            new_cart = ShoppingCart()
            for product in self:
                if product.name not in other.items:
                    new_cart.add_product(product)
            return new_cart
        raise TypeError("Can only subtract another ShoppingCart instance.")

    def __eq__(self, other):
        return isinstance(other, ShoppingCart) and float(self) == float(other)

    def __lt__(self, other):
        return isinstance(other, ShoppingCart) and float(self) < float(other)

    def __le__(self, other):
        return isinstance(other, ShoppingCart) and float(self) <= float(other)

    def __call__(self):
        print("Shopping cart contents:")
        print(self)

    def __rshift__(self, product: Product):
        """Dodaje produkt do koszyka przy użyciu operatora >>."""
        self.add_product(product)
        return self

    def __lshift__(self, product_name: str):
        """Usuwa produkt z koszyka przy użyciu operatora <<."""
        if product_name in self.items:
            del self.items[product_name]
        return self


# Przykład użycia wszystkich metod:
cart1 = ShoppingCart()
cart1 >> Product("Jabłko", 2.5, 4)
cart1 >> Product("Banan", 3.0, 2)
cart1 >> Product("Gruszka", 4.5, 1)

cart2 = ShoppingCart()
cart2 >> Product("Pomarańcza", 5.0, 3)
cart2 >> Product("Winogrona", 10.0, 1)

print("Zawartość koszyka 1:")
print(cart1)
print(f"Wartość koszyka 1: {float(cart1)} PLN")
print(f"Liczba produktów w koszyku 1: {len(cart1)}")

# Sprawdzenie operatorów porównania
print(f"Czy koszyk 1 jest tańszy niż koszyk 2? {cart1 < cart2}")
print(f"Czy koszyk 1 i 2 mają taką samą wartość? {cart1 == cart2}")

# Połączenie koszyków
cart3 = cart1 + cart2
print("Zawartość połączonego koszyka:")
print(cart3)
print(f"Wartość koszyka 3: {float(cart3)} PLN")

# Usunięcie produktu
cart1 << "Jabłko"
print("Zawartość koszyka 1 po usunięciu jabłek:")
print(cart1)

# Dostęp do produktu
print(f"Dostęp do bananów: {cart1['Banan']}")

# Iteracja po produktach
print("Iteracja po produktach w koszyku 3:")
for product in cart3:
    print(product)

# Sprawdzenie, czy produkt jest w koszyku
print(f"Czy 'Winogrona' są w koszyku 3? {'Winogrona' in cart3}")

# Wywołanie instancji koszyka
cart3()
