import csv


class OrdersHandler:
    def __init__(self, file_name):
        self.file_name = file_name
        self.orders = self.load_orders()

    def load_orders(self):
        orders = []
        with open(self.file_name, "r") as file:
            reader = csv.DictReader(file, delimiter=";")
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

        else:
            return None

    def __iter__(self):
        return iter(self.orders)


class Order:
    def __init__(
            self,
            order_id,
            product_name,
            quantity,
            price,
            buyer_name,
            phone,
            email
    ):
        self.order_id = order_id
        self.product_name = product_name
        self.quantity = quantity
        self.price = price
        self.buyer_name = buyer_name
        self.phone = phone
        self.email = email
        self.status = "PENDING"

    def __str__(self):
        return f"{self.order_id} {self.product_name} {self.quantity} {self.price}"

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
            shipping_address
    ):
        super().__init__(
            order_id, product_name, quantity, price, buyer_name, phone, email
        )
        self.shipping_address = shipping_address

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
        super().__init__(order_id, product_name, quantity, price, buyer_name, phone, email, download_link)
        self.subscription_duration = subscription_duration

zamowienia = OrdersHandler("orders.csv")

for zamowienie in zamowienia:
    print(zamowienie)
