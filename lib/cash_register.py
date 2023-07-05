#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount = 0) -> None:
    self.discount = discount
    self.total = 0
    self.items = []
    self.last_item_cost = 0

  def add_item(self, item, price, quantity = 1):
    self.total += (price * quantity)
    self.items += [item] * quantity
    self.last_item_cost = price * quantity

  def apply_discount(self):
    if self.discount != 0:
      self.total *= (1 - (self.discount / 100))
      self.total = int(self.total)
      print(f"After the discount, the total comes to ${self.total}.")
    else:
      print("There is no discount to apply.")

  def void_last_transaction(self):
    self.items.pop()
    self.total -= self.last_item_cost
