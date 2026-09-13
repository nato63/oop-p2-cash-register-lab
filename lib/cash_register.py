#!/usr/bin/env python3


class CashRegister:

    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    def add_item(self, title, price, quantity=1):
        amount = price * quantity
        self.total += amount
        self.items += [title] * quantity
        self.previous_transactions.append(amount)

    def apply_discount(self):
        if self.discount:
            self.total -= self.total * self.discount / 100
            print(f"After the discount, the total comes to ${self._display_total()}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.previous_transactions:
            self.total -= self.previous_transactions.pop()

    def _display_total(self):
        if self.total == int(self.total):
            return int(self.total)
        return self.total
