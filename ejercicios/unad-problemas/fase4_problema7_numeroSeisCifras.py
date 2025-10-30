import os

os.system('cls')


def validar_numero(numero: int):
    """
    Que recibe como parámetro el número y determina si el 
    número es de 6 dígitos, si es de 6 dígitos retorna True 
    de lo contrario retorna False.
    """

    # Validando si el numero ingresado es entero:
    if isinstance(numero, int):
        if len(str(numero)) == 6 and numero > 0:
            # Si el numero contiene 6 digitos y es positivo:
            return True
    return False


def descomponer_numero(numero: int):
    """
    Descomponga un número N de 6 dígitos en tres números de 
    dos dígitos cada uno. Ejemplo: N=121536 -> a=12 b=15 c=36 
    """

    nums_dos_digitos = []
    num = ""

    for digito in str(numero):
        num += digito
        if len(num) == 2:
            nums_dos_digitos.append(num)
            num = ""

    return dict(zip("abc", nums_dos_digitos))


def calcular_tabla(a, b):
    """
    recibe los números a y b y genera la tabla de multiplicar 
    de a hasta b, donde a debe ser menor que b. 
    """

    print(f"- Tabla de multiplicar de a = {a} hasta b = {b}:\n")

    a, b = int(a), int(b)
    if a < b:
        for m in range(a, b + 1):
            for n in range(1, 11):
                print(f"{m} x {n} = {m * n}", end=", ")
            print("")

    else:
        print("  No se puede mostrar la tabla porque a >= b.")


def unir(a: int, c: int):
    """
    recibe a y c y debe retornar un solo número resultado de 
    unir a y c el número devuelto debe quedar de 4 cifras 
    Ejemplo: a=12 c=36 número queda =1236 
    """
    return int(a + c)


def principal():
    while True:
        try:
            numero_usuario = int(input("Ingrese un numero de 6 digitos: "))
            if validar_numero(numero_usuario):
                break
            print("Error: El numero debe tener 6 digitos.\n")
        except ValueError:
            print("Error: Ingrese solo numeros por favor.\n")

    print(f"\n- Numero Ingresado: {numero_usuario}\n")

    numeros_separados = descomponer_numero(numero_usuario)
    print(f"- Numero Descompuesto: {numeros_separados}\n")
    num_a = numeros_separados["a"]
    num_b = numeros_separados["b"]
    num_c = numeros_separados["c"]
    calcular_tabla(num_a, num_b)
    print(f"\n- Union a = {num_a} y c = {num_c}: {unir(num_a, num_c)}\n")


if __name__ == "__main__":
    principal()

    input("\nPresione ENTER para salir.\n")
