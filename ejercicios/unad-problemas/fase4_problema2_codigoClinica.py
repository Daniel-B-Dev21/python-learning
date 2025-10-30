import os

os.system('cls')

# Creando un diccionario con los servicios y sus costos:
servicios = {
    1: {"RADIOGRAFIA": 30000},
    2: {"ECOGRAFIA": 35000},
    3: {"LABORATORIO": 25000},
    4: {"CONSULTA EXTERNA": 40000},
    5: {"CONSULTA ESPECIALIZADA": 80000}
}


def validar_codigo(codigo: int):
    """
    Recibe como parámetro un número entero, retorna True sí 
    el número tiene 5 dígitos, en caso de no cumplir retorna False, 
    para indicar que no es válido
    """
    # Validando si el codigo ingresado es entero:
    if isinstance(codigo, int):
        if len(str(codigo)) == 5 and codigo > 0:
            # Si el numero contiene 5 digitos:
            return True
    return False


def tipo(codigo: int):
    """
    Recibe como parámetro un número entero, sí el primer dígito es 1 
    retorna "AFILIADO", pero sí es 2 retorna "PARTICULAR", 
    dato de tipo string. 
    """

    if int(str(codigo)[0]) == 1:
        return "AFILIADO"
    if int(str(codigo)[0]) == 2:
        return "PARTICULAR"
    return "TIPO NO DEFINIDO"


def servicio(codigo: int):
    """
    Recibe como parámetro un número entero, el segundo dígito permite 
    retornar el nombre del procedimiento a realizar.
    Ejemplo: sí el dígito es 3 retorna "LABORATORIO" 
    """

    segundo_digito = int(str(codigo)[1])
    resultado = servicios.get(segundo_digito)

    if resultado is not None:
        for s in resultado:
            return s

    return "SERVICIO NO DEFINIDO"


def costo(nombre_servicio: str):
    """
    Recibe como parámetro un dato de tipo string con el nombre del servicio 
    a realizar, con base a este se determinar el costo base. 
    Ejemplo: sí recibe "LABORATORIO" se retorna 25000. 
    """

    if isinstance(nombre_servicio, str):
        servicio_costos = {}

        for s in servicios.values():
            for nombre, precio in s.items():
                servicio_costos[nombre] = precio
        return servicio_costos.get(nombre_servicio, float(0))

    return float(0)


def calcular_descuento_recargo(codigo: int, tipo_paciente: str, costo_servicio: int):
    """
    Recibe como parámetro un número entero (el código), un dato de tipo string 
    con el tipo de paciente y un dato de tipo entero con el costo del procedimiento, 
    y calcula el valor del descuento o recargo. 
    """

    ultimos_3_digitos = []

    codigo_string = str(codigo)

    for i in range(5):
        if i in (2, 3, 4):
            ultimos_3_digitos.append(int(codigo_string[i]))

    suma_3_digitos = sum(ultimos_3_digitos)

    if suma_3_digitos % 2 == 0:
        if tipo_paciente == "AFILIADO":
            return float(-(costo_servicio * 0.15))

        if tipo_paciente == "PARTICULAR":
            return float(costo_servicio * 0.15)

        return float(0)

    if tipo_paciente == "AFILIADO":
        return float(-(costo_servicio * 0.25))

    if tipo_paciente == "PARTICULAR":
        return float(costo_servicio * 0.25)

    return float(0)


def pago_total(costo_base: int, desc_rec: float):
    """
    Recibe como parámetro un número entero correspondiente al costo base 
    del servicio y un número float correspondiente al descuento o recargo 
    que se aplicara, la función retorna el valor final a pagar por el servicio. 
    """

    if not isinstance(costo_base, str):
        return costo_base + desc_rec
    return float(0)


def principal():
    """
    programa principal
    """
    while True:
        try:
            codigo_usuario = int(input("Ingrese su codigo de 5 digitos: "))
            if validar_codigo(codigo_usuario):
                break
            print("Error: El numero debe tener 5 digitos (no negativo).\n")
        except ValueError:
            print("Error: Ingrese solo numeros por favor.\n")

    tipo_usuario = tipo(codigo_usuario)
    servicio_usuario = servicio(codigo_usuario)
    costo_servicio_usuario = costo(servicio_usuario)
    calculo_desc_rec = calcular_descuento_recargo(
        codigo_usuario, tipo_usuario, costo_servicio_usuario)

    total_a_pagar_usuario = pago_total(
        costo_servicio_usuario, calculo_desc_rec)

    print("\nFACTURA PACIENTE\n")
    print(f"- Tipo: {tipo_usuario}")
    print(f"- Servicio: {servicio_usuario}")
    print(f"- Costo Servicio: {costo_servicio_usuario}")

    if calculo_desc_rec > 0:
        item = "Recargo"
    else:
        item = "Descuento"

    print(f"- Valor del {item}: {calculo_desc_rec}")
    print(f"\nTotal a pagar: {total_a_pagar_usuario}")


if __name__ == "__main__":
    principal()

    input("\nPresione ENTER para salir.\n")
