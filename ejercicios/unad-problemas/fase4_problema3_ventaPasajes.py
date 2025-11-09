"""
a. Cúcuta
i. Primera clase: 20000
ii. Segunda clase: 15000
iii. Tercera clase: 12000
b. Bucaramanga
i. Primera clase: 30000
ii. Segunda clase: 25000
iii. Tercera clase: 20000
c. Bochalema
i. Primera clase: 10000
ii. Segunda clase: 8000
iii. Tercera clase:5000

"""


import os

os.system('cls')

DB_PASAJES = {
    1: {
        "Cucuta": {
            "clase1": 20000,
            "clase2": 15000,
            "clase3": 12000
        }
    },

    2: {
        "Bucaramanga": {
            "clase1": 30000,
            "clase2": 25000,
            "clase3": 20000
        }
    },

    3: {
        "Bochalema": {
            "clase1": 10000,
            "clase2": 8000,
            "clase3": 5000
        }
    }
}


def menu_principal():
    print("=" * 30)
    print("SISTEMA DE VIAJES")
    print("=" * 30)

    print("\n1. Vender pasaje.\n2. Salir\n")

    while True:
        try:
            opcion = int(input("¿Cual es su opcion?: "))
            if opcion in (1, 2):
                return opcion
            print("Opcion no valida")
        except ValueError:
            print("Opcion no valida")


def datos():

    datos_destino = {"id": 0, "clase": 0}

    print("COMPRA DE BOLETOS")
    print("\nEscoja un destino:\n\n1. Cucuta\n2. Bucaramanga\n3. Bochalema\n")

    while True:
        try:
            destino_opcion = int(input("Escriba el numero de destino (1-3): "))
            if destino_opcion in (1, 2, 3):
                datos_destino["id"] += destino_opcion
                break
            if destino_opcion == 0:
                break
            print("Opcion no valida")
        except ValueError:
            print("Opcion no valida")

    if destino_opcion:
        datos_destino_base = DB_PASAJES[destino_opcion]

        for k, v in datos_destino_base.items():
            print("\nDestino elegido:", k, "\n")
            for m, n in v.items():
                print(f"- {m.upper()}: ${n}")

        while True:
            try:
                clase_opcion = int(
                    input("\nEscriba el numero de clase (1-3): "))
                if clase_opcion in (1, 2, 3):
                    datos_destino["clase"] += clase_opcion
                    break
                if clase_opcion == 0:
                    break
                print("Opcion no valida")
            except ValueError:
                print("Opcion no valida")

    return datos_destino


def valor_pasaje(datos_destino: dict):

    id_destino = datos_destino['id']
    clase_destino = datos_destino['clase']

    if id_destino:
        db_datos = DB_PASAJES[id_destino]
        nombre_destino = (list(db_datos))[0]
        clases = db_datos[nombre_destino]

        if clase_destino:
            clase_destino = "clase" + str(clase_destino)
            return clases[clase_destino]
    return 0


def descuento(cant_pasajes: int):
    """
    La empresa ofrece descuentos por cantidad de pasajes, así: menos
    de 5 pasajes 0%, 6 a 12 pasajes 10% y más de 12 20%.
    """

    if cant_pasajes > 0:
        if cant_pasajes <= 5:
            return float(0)
        if 6 <= cant_pasajes <= 12:
            return 0.1
        return 0.2

    return float(0)


def pago(cant_pasajes: int, pago_pasaje: int, valor_descuento: float):
    """
    Calcula el total a pagar aplicando el descuento.
    """

    total_base = cant_pasajes * pago_pasaje
    monto_descuento = total_base * valor_descuento

    return total_base - monto_descuento
