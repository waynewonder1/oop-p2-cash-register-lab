#!/usr/bin/env python3


class CashRegister:

    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, discount):
        # discount is a percentage (0-100) taken off the total, not a raw amount
        if isinstance(discount, int) and 0 <= discount <= 100:
            self._discount = discount
        else:
            print("Not valid discount")
            self._discount = 0

    def add_item(self, item, price, quantity=1):
        self.total += price * quantity
        self.items += [item] * quantity
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
        else:
            self.total -= self.total * self.discount / 100
            # :g avoids printing whole-dollar totals like "800.0"
            print(f"After the discount, the total comes to ${self.total:g}.")

    def void_last_transaction(self):
        if not self.previous_transactions:
            print("There is no transaction to void.")
        else:
            last_transaction = self.previous_transactions.pop()
            price = last_transaction["price"]
            quantity = last_transaction["quantity"]
            self.total -= price * quantity
            # drop the last `quantity` entries added by that transaction
            self.items = self.items[:-quantity]
