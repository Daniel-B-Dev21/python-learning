import os

os.system('cls')

TIPO_LIBRO = {
    1: {
        "TIPO": "General",
        "DIAS": 8,
        "PAGO": 500,
        "CONTADOR_PRESTAMO": 0
    },

    2: {
        "TIPO": "Coleccion",
        "DIAS": 3,
        "PAGO": 1000,
        "CONTADOR_PRESTAMO": 0
    },

    3: {
        "TIPO": "Reserva",
        "DIAS": 1,
        "PAGO": 5000,
        "CONTADOR_PRESTAMO": 0
    }
}


def validar_codigo(codigo_libro):
    """
    Debe recibir el código del libro y este debe 
    cumplir: ser un número de 6 dígitos, el primer dígito corresponde 
    al tipo (1. General 2. Colección 3. Reserva) los 3 siguientes al área 
    que debe estar entre 101 y 108. Si cumple debe retornar un 
    1(uno), si no cumple debe retornar un 0 (cero)
    """

    codigo_libro = str(codigo_libro)

    if len(codigo_libro) == 6:
        if int(codigo_libro[0]) in (1, 2, 3):
            sig_tres_digitos = int(
                codigo_libro[1] + codigo_libro[2] + codigo_libro[3])

            return 101 <= sig_tres_digitos <= 108
    return False


def prestamo(codigo_libro):
    """
    La función debe recibir el código del libro, y sí es 
    válido retorna la cantidad de días que puede ser prestado, siendo 8 
    días para los del área General, 3 para los de Colección y 1 para los 
    de Reserva, sí no es válido retorna 0. 
    """

    if validar_codigo(codigo_libro):
        datos_libro = TIPO_LIBRO[int(str(codigo_libro)[0])]
        return datos_libro.get("DIAS", 0)
    return 0


def recoleccion(codigo_libro):
    """
    La función debe recibir el código del libro, y sí es 
    válido retorna el valor a pagar por el usuario, así: $500 por los 
    del área General, $1.000 por los de Colección y $5.000 por los de 
    Reserva, sí no es válido retorna 0
    """

    if validar_codigo(codigo_libro):
        datos_libro = TIPO_LIBRO[int(str(codigo_libro)[0])]
        return datos_libro.get("PAGO", 0)
    return 0


def registrar_prestamo(codigo_libro):
    """
    """

    if validar_codigo(codigo_libro):
        primer_digito = int(str(codigo_libro)[0])
        TIPO_LIBRO[primer_digito]["CONTADOR_PRESTAMO"] += 1
        print("Libro prestado Exitosamente")
        return True
    return False


def dinero_recolectado():
    """
    """

    for i, datos in TIPO_LIBRO.items():
        total = datos["PAGO"] * datos["CONTADOR_PRESTAMO"]
        print(i, total)


def menu():
    """
    Menu principal.
    """

    print("BIBLIOTECA LEXUS\n\n1. Prestamos\n2. Recoleccion\n3. Salir\n\n")

    while True:
        try:
            opcion_usuario = int(input("Seleccione una opcion (1-3): "))
            if opcion_usuario in (1, 2, 3):
                return opcion_usuario
            print("Opcion no valida.")
        except ValueError:
            print("Ingrese solo numeros de 1-3")


def execution():
    while True:
        opcion = menu()
        codigo_libro = input("Ingrese el codigo del libro (6 digitos): ")

        if opcion == 1:
            registrar_prestamo(codigo_libro)
            print(
                f"Libro con codigo {codigo_libro} prestado por {prestamo(codigo_libro)} dias.")

        elif opcion == 2:
            dinero_recolectado()

        else:
            print("Saliendo...\n")
            break


if __name__ == "__main__":
    execution()
