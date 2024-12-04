class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0.0
        self.items = []
        self.last_transaction = None

    def add_item(self, item_name, price, quantity=1):
        self.total += price * quantity
        for _ in range(quantity):
            self.items.append(item_name)
        self.last_transaction = {"price": price, "quantity": quantity}

    def apply_discount(self):
        if self.discount > 0:
            self.total = round(self.total * (1 - self.discount / 100), 2)
            total_str = f"{self.total:.2f}".rstrip('0').rstrip('.')
            print(f"After the discount, the total comes to ${total_str}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.last_transaction:
            self.total -= self.last_transaction["price"] * self.last_transaction["quantity"]
            self.last_transaction = None
            if not self.items:
                self.total = 0.0
        else:
            print("No transactions to void.")
