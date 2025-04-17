#how factory design pattern works
from abc import ABC, abstractmethod

#Defining Product Interface
class Coffee(ABC) :
  @abstractmethod
  def prepare(self):
    pass

#Implement Concrete Products
class Espresso(Coffee):
  def prepare(self):
    return "Preparing Espresso"

class Latte(Coffee):
  def prepare(self):
    return "Preparing Latte"

class Cappuccino(Coffee):
  def prepare(self):
    return "Preparing Cappuccino"

#Implementing the factory (CoffeeMachine)
class CoffeeMachine:
  def make_coffee(self, coffee_type):
    if coffee_type == "Espresso":
      return Espresso().prepare()
    if coffee_type == "Latte":
      return Latte().prepare()
    if coffee_type == "Cappuccino":
      return Cappuccino().prepare()
    else :
      return "Unknown Coffee Type"


#Use the Factory to Create Products
if __name__ == "__main__":
  machine = CoffeeMachine()
  coffee = machine.make_coffee("Espresso")
  print(coffee)
  coffee = machine.make_coffee("Latte")
  print(coffee)
  coffee = machine.make_coffee("Cappuccino")
  print(coffee)
