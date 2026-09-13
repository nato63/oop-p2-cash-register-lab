#!/usr/bin/env python3


class CashRegister:

    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self._last_transaction_total = 0
        self._last_transaction_quantity = 0

    def add_item(self, title, price, quantity=1):
        self.items += [title] * quantity
        self._last_transaction_total = price * quantity
        self._last_transaction_quantity = quantity
        self.total += self._last_transaction_total

    def apply_discount(self):
        if self.discount:
            self.total -= self.total * self.discount / 100
            print(f"After the discount, the total comes to ${self._display_total()}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        self.total -= self._last_transaction_total
        if self._last_transaction_quantity:
            del self.items[-self._last_transaction_quantity :]
        self._last_transaction_total = 0
        self._last_transaction_quantity = 0

    def _display_total(self):
        if self.total == int(self.total):
            return int(self.total)
        return self.total
