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
        Add product to Shop inventory, or update.
        """

        self.inventory[category][product.id_product] = product

    def remove_product(self, category_name, id_product):
        """
        Delete product from inventory.
        """
        if id_product in self.inventory[category_name]:
            del self.inventory[category_name][id_product]
            return True
        return False


class Product:

    def __init__(self, id_product, name, price, stock):
        self.id_product = id_product
        self.name = name
        self.price = price
        self.stock = stock


class Customer:

    def __init__(self, id_customer, name, email) -> None:
        self.id_customer = id_customer
        self.name = name
        self.email = email
        self.shopping_cart = []

    def add_product_to_cart(self, product):
        """Add product to shopping cart"""

        if not product in self.shopping_cart:
            self.shopping_cart.append(product)

        else:
            index = 0
            for i in self.shopping_cart:
                if i == product:
                    item = self.shopping_cart[index]
                    item.stock += product.stock
                    return True
                index += 1


my_shop = Shop(13758821, "Apple Store")
my_shop.add_category("technology")

item_1 = Product("P100", "iPhone 17 Pro Max", 3225.12, 523)
item_2 = Product("P101", "Macbook Pro 12", 5400.5, 130)

my_shop.add_product(item_1, "technology")
my_shop.add_product(item_2, "technology")

my_customer = Customer("C100", "Daniel", "daniel@email.com")
my_customer.add_product_to_cart(item_1)
my_customer.add_product_to_cart(item_1)
