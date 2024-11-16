from pprint import pprint

class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop():
    __file_name = 'products.txt'

    def get_products(self):
        with open('products.txt') as file:
            s = file.read()
            file.close()
        return s

    def add(self, *products):
        self.products = products
        spisok_productov = self.get_products()

        for i in products:
            if str(i) not in spisok_productov:
                file = open('products.txt', 'a')
                file.write(f'{i}\n')
                file.close()

            else:
                print(f'Продукт {i} уже есть в магазине')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__
s1.add(p1, p2, p3)
print(s1.get_products())