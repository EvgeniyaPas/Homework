from pprint import pprint

from unicodedata import category


class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop(Product):
    __file_name = 'products.txt'

    def get_products(self):
        file = open ('products.txt', 'r')
        pprint(file.read())
        file.close()

    def add(self, *products):
        self.products = products
        print(*products)
        # super().__init__()
        file = open('products.txt', 'r')
        for self.name in  file:
            print(f'Продукт {self.products} уже есть в магазине')
            file.close()

        else:
            file = open('products.txt', 'a')
            file.write(f'{self.name}, {self.weight}, {self.category}')
            file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__
print(s1.get_products())

s1.add(p1, p2, p3)

print(s1.get_products())

