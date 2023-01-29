from project.food import Food
from project.drink import Drink


class ProductRepository:

    def __init__(self):
        self.products = []

    def add(self, product):
        self.products.append(product)

    def find(self, product_name):
        for product in self.products:
            if product.name == product_name:
                return product

    def remove(self, product_name):
        p = self.find(product_name)
        if p:
            self.products.remove(p)

    def __repr__(self):
        result = '\n'.join([f"{product}: {product.quantity}" for product in self.products])
        return result

food = Food("apple")
drink = Drink("water")
repo = ProductRepository()
repo.add(food)
repo.add(drink)
print(repo.products)
print(repo.find("water"))
repo.find("apple").decrease(5)
print(repo)
