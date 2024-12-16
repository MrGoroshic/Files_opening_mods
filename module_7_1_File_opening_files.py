from pprint import pprint

class Product:
    def __init__(self, name:str, weight:float, category:str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    __file_name = "mod_7_1.txt"

    def get_products(self):
        file = open(self.__file_name, "r")
        task = file.read()
        file.close()
        return task

    def add(self, *products):
        task = self.get_products()
        file = open(self.__file_name, "a")
        for prod in products:
            if prod.name in task:
                print(f"Продукт {prod.name} уже есть в магазине")
            else:
                file.write(f"{prod.name}, {prod.weight}, {prod.category}\n")
        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())