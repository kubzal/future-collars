# ### Zadanie: System zamówień w sklepie internetowym

# Twoim zadaniem jest napisanie programu w Pythonie, który symuluje system zarządzania zamówieniami w sklepie internetowym. Program będzie wczytywał dane zamówień z pliku CSV, przetwarzał zamówienia i tworzył codzienny raport z informacjami o liczbie przetworzonych produktów oraz o zyskach.

# #### Wymagania:
# 1. **Plik CSV**: W pliku CSV zamówienia są zapisane przy użyciu średnika (`;`) jako separatora. Plik zawiera następujące kolumny:
#    - `Order ID`: Unikalny numer zamówienia
#    - `Product Name`: Nazwa produktu
#    - `Quantity`: Ilość zamówionych produktów
#    - `Price`: Cena jednostkowa produktu
#    - `Order Type`: Typ zamówienia (może przyjmować wartości `Physical`, `Digital`, lub `Subscription`)
#    - `Buyer Name`: Imię i nazwisko kupującego
#    - `Phone`: Numer telefonu kupującego
#    - `Email`: Adres e-mail kupującego
#    - `Shipping Address`: Adres wysyłki (dla produktów fizycznych)
#    - `Additional Info`: Dodatkowe informacje, np. link do pobrania lub czas trwania subskrypcji.

# 2. **Klasy produktów**:
#    - Klasa `Order`: klasa bazowa, reprezentująca ogólne zamówienie. Każde zamówienie powinno posiadać atrybuty takie jak `order_id`, `product_name`, `quantity`, `price`, `buyer_name`, `phone`, `email` oraz `status`, który domyślnie ustawiony jest na `PENDING`.
#    - Klasy pochodne:
#      - `PhysicalProduct`: dziedziczy po `Order`, dodatkowo posiada atrybut `shipping_address` i zmienia status na `SHIPPED_TO_ADDRESS` po przetworzeniu zamówienia.
#      - `DigitalProduct`: dziedziczy po `Order`, dodatkowo posiada atrybut `download_link` i zmienia status na `EMAIL_SENT` po przetworzeniu zamówienia.
#      - `SubscriptionProduct`: dziedziczy po `DigitalProduct`, dodatkowo posiada atrybut `subscription_duration` (czas trwania subskrypcji).

# 3. **Przetwarzanie zamówień**:
#    - Każde zamówienie powinno mieć metodę `process_order`, która zmienia status zamówienia i wypisuje odpowiednie informacje (np. adres wysyłki lub link do pobrania).

# 4. **Tworzenie raportu**:
#    - Klasa `OrdersHandler` powinna być iterowalna, a jej metoda `daily_report` ma generować plik CSV z informacjami o:
#      - Liczbie wysłanych produktów fizycznych, cyfrowych i aktywowanych subskrypcji.
#      - Łącznym zysku ze wszystkich zamówień.
#    - Plik z raportem powinien być zapisywany z nazwą zawierającą dzisiejszą datę, np. `daily_report_2024-10-16.csv`.

# 5. **Dane przykładowe**:
#    - Plik CSV powinien zawierać około 15 przykładowych zamówień, z różnymi typami produktów i polskimi danymi klientów.


import csv
from datetime import datetime


class OrdersHandler:
    def __init__(self, file_name):
        self.file_name = file_name
        self.orders = self.load_orders()

    def load_orders(self):
        orders = []
        with open(self.file_name, mode="r") as file:
            reader = csv.DictReader(file, delimiter=";")  # Użycie separatora ";"
            for row in reader:
                order = self.create_order(row)
                if order:
                    orders.append(order)
        return orders

    def create_order(self, row):
        order_id = int(row["Order ID"])
        product_name = row["Product Name"]
        quantity = int(row["Quantity"])
        price = float(row["Price"])
        buyer_name = row["Buyer Name"]
        phone = row["Phone"]
        email = row["Email"]
        shipping_address = row["Shipping Address"]
        order_type = row["Order Type"]
        additional_info = row["Additional Info"]

        if order_type == "Physical":
            return PhysicalProduct(
                order_id,
                product_name,
                quantity,
                price,
                buyer_name,
                phone,
                email,
                shipping_address,
            )
        elif order_type == "Digital":
            return DigitalProduct(
                order_id,
                product_name,
                quantity,
                price,
                buyer_name,
                phone,
                email,
                additional_info,
            )
        elif order_type == "Subscription":
            download_link, subscription_duration = additional_info.split(" - ")
            subscription_duration = int(subscription_duration.split()[0])
            return SubscriptionProduct(
                order_id,
                product_name,
                quantity,
                price,
                buyer_name,
                phone,
                email,
                download_link,
                subscription_duration,
            )
        return None

    def __iter__(self):
        return iter(self.orders)

    def daily_report(self):
        total_physical = 0
        total_digital = 0
        total_subscription = 0
        total_revenue = 0.0

        for order in self.orders:
            if order.status == "SHIPPED_TO_ADDRESS":
                total_physical += order.quantity
            elif order.status == "EMAIL_SENT":
                if isinstance(order, SubscriptionProduct):
                    total_subscription += order.quantity
                else:
                    total_digital += order.quantity
            total_revenue += order.quantity * order.price

        report_file_name = f"daily_report_{datetime.now().strftime('%Y-%m-%d')}.csv"
        with open(report_file_name, mode="w", newline="") as file:
            writer = csv.writer(file, delimiter=";")  # Użycie separatora ";"
            writer.writerow(
                [
                    "Total Physical Products Shipped",
                    "Total Digital Products Sent",
                    "Total Subscriptions Activated",
                    "Total Revenue",
                ]
            )
            writer.writerow(
                [
                    total_physical,
                    total_digital,
                    total_subscription,
                    f"${total_revenue:.2f}",
                ]
            )

        print(f"Daily report saved to {report_file_name}.")
        print(
            f"Summary: Physical: {total_physical}, Digital: {total_digital}, Subscription: {total_subscription}, Revenue: ${total_revenue:.2f}"
        )


class Order:
    def __init__(
        self, order_id, product_name, quantity, price, buyer_name, phone, email
    ):
        self.order_id = order_id
        self.product_name = product_name
        self.quantity = quantity
        self.price = price
        self.buyer_name = buyer_name
        self.phone = phone
        self.email = email
        self.status = "PENDING"

    def process_order(self):
        print(
            f"Processing order #{self.order_id} for {self.quantity} unit(s) of {self.product_name}."
        )
        self.status = "PROCESSED"


class PhysicalProduct(Order):
    def __init__(
        self,
        order_id,
        product_name,
        quantity,
        price,
        buyer_name,
        phone,
        email,
        shipping_address,
    ):
        super().__init__(
            order_id, product_name, quantity, price, buyer_name, phone, email
        )
        self.shipping_address = shipping_address

    def process_order(self):
        super().process_order()
        self.status = "SHIPPED_TO_ADDRESS"
        print(f"Shipping to: {self.shipping_address}")


class DigitalProduct(Order):
    def __init__(
        self,
        order_id,
        product_name,
        quantity,
        price,
        buyer_name,
        phone,
        email,
        download_link,
    ):
        super().__init__(
            order_id, product_name, quantity, price, buyer_name, phone, email
        )
        self.download_link = download_link

    def process_order(self):
        super().process_order()
        self.status = "EMAIL_SENT"
        print(f"Download link: {self.download_link}")


class SubscriptionProduct(DigitalProduct):
    def __init__(
        self,
        order_id,
        product_name,
        quantity,
        price,
        buyer_name,
        phone,
        email,
        download_link,
        subscription_duration,
    ):
        super().__init__(
            order_id,
            product_name,
            quantity,
            price,
            buyer_name,
            phone,
            email,
            download_link,
        )
        self.subscription_duration = subscription_duration

    def process_order(self):
        super().process_order()
        print(f"Subscription for {self.subscription_duration} month(s)")


# Stwórz obiekt OrdersHandler i wypisz wszystkie zamówienia
orders_handler = OrdersHandler("orders.csv")

# Procesowanie zamówień
for order in orders_handler:
    order.process_order()

# Tworzenie raportu
orders_handler.daily_report()
