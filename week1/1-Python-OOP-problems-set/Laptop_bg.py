class Product:

    def __init__(self, name, stock_prize, final_prize):
        self.name = name
        self.stock_prize = stock_prize
        self.final_prize = final_prize

    def profit(self):
        return self.final_prize - self.stock_prize


class Laptop(Product):

    def __init__(self, name, stock_prize, final_prize, diskspace, ram):
        super().__init__(name, stock_prize, final_prize)
        self.diskspace = diskspace
        self.ram = ram


class Smartphone(Product):

    def __init__(self, name, stock_prize, final_prize, display_size, mega_pixels):
        super().__init__(name, stock_prize, final_prize)
        self.display_size = display_size
        self.mega_pixels = mega_pixels


class Store:

    def __init__(self, name):
        self.name = name
        self.products = {}
        self.store_profit = 0

    def load_new_products(self, product, count):
        if product in self.products:
            self.products[product] += count
        else:
            self.products[product] = count

    def list_products(self, product_class):
        for product in self.products:
            if isinstance(product, product_class):
                print("{} - {} count".format(product.name, self.products[product]))

    def sell_product(self, product):
        if product in self.products:
            if self.products[product] > 0:
                self.products[product] -= 1
                self.store_profit += product.profit()
                return True

        return False

    def total_income(self):
        return self.store_profit


new_product = Product('HP HackBook', 1000, 1243)
new_product.profit()
new_laptop = Laptop('HP HackBook', 1000, 1243, 1000, 4)
new_smarthphone = Smartphone('Hack Phone', 500, 820, 7, 10)
new_store = Store('Laptop.bg')
new_store.load_new_products(new_laptop, 20)
new_store.sell_product(new_laptop)
new_store.sell_product(new_laptop)
new_store.total_income()
new_store.list_products(Laptop)
