class Shop:

    def __init__(self, nit, name) -> None:
        self.nit = nit
        self.name = name
        self.inventory = {}

    def add_category(self, category_name):
        """
        Add category to inventory shop.
        """

        if self.inventory.get(category_name, None) is None:
            self.inventory[category_name] = {}

    def add_product(self, product, category):
        """
        Add product to Shop inventory.
        """

        self.inventory[category][product.id_product] = {
            "name": product.name,
            "price": product.price,
            "stock": product.stock
        }

    def remove_product(self, id_product):
        pass

    def update_product(self, id_product):
        pass


class Product:

    def __init__(self, id_product, name, price, stock):
        self.id_product = id_product
        self.name = name
        self.price = price
        self.stock = stock


my_shop = Shop(13758821, "Apple Store")
my_shop.add_category("technology")

item_1 = Product("P100", "iPhone 17 Pro Max", 3225.12, 523)
item_2 = Product("P101", "Macbook Pro 12", 5400.5, 130)

my_shop.add_product(item_1, "technology")
my_shop.add_product(item_2, "technology")


print(my_shop.inventory)
