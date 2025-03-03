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


# Przykład użycia:
cart1 = ShoppingCart()
cart1 >> Product("Jabłko", 2.5, 4)
cart1 >> Product("Banan", 3.0, 2)

cart2 = ShoppingCart()
cart2 >> Product("Pomarańcza", 5.0, 3)

print(cart1)  # Wypisanie zawartości koszyka
print(f"Wartość koszyka: {float(cart1)} PLN")  # Konwersja na float

cart3 = cart1 + cart2  # Łączenie koszyków
print(cart3)
print(f"Koszyk 3: {int(cart3)} PLN")

cart1()  # Wywołanie instancji klasy

cart1 << "Jabłko"  # Usunięcie jabłek z koszyka
print(cart1)
