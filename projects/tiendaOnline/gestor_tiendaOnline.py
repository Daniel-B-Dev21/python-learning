import os

os.system('cls')


class Producto:

    def __init__(self, id, nombre, precio, stock) -> None:
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def mostrar_info(self):
        """
        Muestra toda la informacion del producto.
        """

        print(
            f"Id: {self.id}, Nombre: {self.nombre}, Precio: {self.precio}, Stock: {self.stock}")

    def actualizar_stock(self, cantidad):
        """
        Actualiza el stock del producto, si la cantidad es entera positiva,
        aumenta el stock, de lo contrario, si es negativa lo disminuye."
        """

        if cantidad < 0:
            if (cantidad * -1) > self.stock:
                raise ValueError(
                    "Candidad ingresada mayor a unidades disponibles.")

        self.stock += cantidad
        print("Stock actualizado con exito.")

        return True


class Cliente:

    def __init__(self, id, nombre, email):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.carrito = []

    def agregar_al_carrito(self, producto, cantidad):
        """
        Agrega un producto al carrito del cliente.
        """

        if len(self.carrito) > 0:
            for cliente_producto in self.carrito:
                if producto in cliente_producto:
                    cliente_producto[1] += cantidad
                    return True

        self.carrito.append([producto, cantidad])
        return True

    def eliminar_del_carrito(self, producto):
        """
        Elimina un producto del carrito del cliente.
        """
        for p in self.carrito:
            if producto in p:
                self.carrito.remove(p)
                return True
        return False

    def ver_carrito(self):
        """
        Muestra los productos del carrito del cliente.
        """
        if len(self.carrito) > 0:
            print(
                f"Carrito de {self.nombre} con {len(self.carrito)} productos :D\n")
            contador = 1

            for p in self.carrito:
                print(f"Producto {contador}:")
                p[0].mostrar_info()
                print(f"Cantidad: {p[1]}\n")
                contador += 1
            return True
        print(f"Carrito de {self.nombre} vacio :(")

    def realizar_compra(self):
        """
        Si el carrito de compras contiene productos, calcula el total a pagar.
        """

        if len(self.carrito) > 0:
            total_compra = 0

            for p in self.carrito:
                p[0].actualizar_stock(p[1] * -1)
                total_compra += (p[0].precio * p[1])

            print(f"\nTotal a pagar: ${total_compra}")
            self.carrito = []
            return True

        return False


arroz = Producto(1, "arroz", 10000, 50)
papas = Producto(2, "papas", 8000, 110)
cliente = Cliente("c1", "Daniel", "daniel@email.com")

cliente.agregar_al_carrito(arroz, 12)
cliente.agregar_al_carrito(papas, 12)
cliente.agregar_al_carrito(papas, 13)
cliente.ver_carrito()
cliente.realizar_compra()
cliente.ver_carrito()

arroz.mostrar_info()
papas.mostrar_info()
