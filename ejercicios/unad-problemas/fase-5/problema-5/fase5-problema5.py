REGISTRO = {}


def registro_notas():
    """
    Registra 3 notas para cada estudiante.
    """
    notas = []

    for n in range(1, 4):
        while True:
            try:
                nota = float(input(f"Nota {n}: "))
                if 0 <= nota <= 100:
                    break
                print("Debe ingresar una nota en el rango de 0 y 100.")
            except ValueError:
                print("Ha escrito una nota no valida.")

        notas.append(nota)

    return notas


def registro_estudiantes():
    """
    Agrega a los estudiantes con sus respectivas notas y promedio al registro.
    """

    print("\nREGISTRO DE ESTUDIANTES\n")

    while True:
        try:
            num_estudiantes = int(input('Numero de estudiantes a registrar: '))
            if num_estudiantes > 0:
                break
            print("Debe ingresar un numero mayor a cero.")
        except ValueError:
            print("Ha escrito un valor no valido.")

    for num in range(1, num_estudiantes + 1):
        print(f"\nEstudiante {num}:\n")

        while True:
            nombre = input("Nombre del Estudiante: ").capitalize()
            if not nombre in REGISTRO:
                break
            print(f"El estudiante '{nombre}' ya se encuentra registrado(a).")

        notas = registro_notas()
        promedio = round(sum(notas) / len(notas), 2)
        REGISTRO[nombre] = {"notas": notas, "promedio": promedio}
        print(f"\nEl estudiante {nombre} se ha registrado exitosamente.")

    print(f"\nSe han registrado {num_estudiantes} estudiantes exitosamente.")


def ranking_estudiantes(registro):
    """
    Calcula y muestra el ranking de estudiantes (Mejor promedio, ordenados 
    de manera descendente y promedio general).
    """
    if len(registro) > 0:

        promedios = {}

        for estudiante, datos in registro.items():
            promedios[estudiante] = datos['promedio']

        solo_promedios = list(promedios.values())
        # Ordenando la lista de manera descendente con el método sorted():
        solo_promedios = sorted(solo_promedios, reverse=True)

        maximo_promedio = max(solo_promedios)
        promedio_general = round(sum(solo_promedios)/len(solo_promedios), 2)

        resultados = {}
        ranking_promedio = []

        for p in solo_promedios:
            for nombre, promedio in promedios.items():
                if p == maximo_promedio:
                    resultados["mejor promedio"] = nombre

                if p == promedio:
                    ranking_promedio.append(nombre)
                    break

        resultados["ranking"] = ranking_promedio
        resultados["promedio general"] = promedio_general

        # mostrando los resultados:
        print("\nRESULTADOS:\n")
        print(f"Promedios Obtenidos: {promedios}\n")
        for clave, valor in resultados.items():
            print(f"- {clave.capitalize()}: {valor}")

        return True

    print("\nNo se ha registrado ningún estudiante.")
    return False


def menu():
    print("REGISTRO DE NOTAS\n")
    print("1. Registrar Notas\n2. Generar Ranking\n3. Salir")

    while True:
        opcion = input("\nSeleccione una opción (1-3): ")
        if opcion in ("1", "2", "3"):
            return opcion

        print("Ingrese una opción valida.")


def main():
    """
    Programa principal.
    """

    while True:
        opcion = int(menu())

        if opcion == 1:
            registro_estudiantes()
        elif opcion == 2:
            ranking_estudiantes(REGISTRO)
        elif opcion == 3:
            input("\nPresione ENTER para continuar.")
            print("\n")
            break

        input("\nPresione ENTER para volver al menu.")
        print("\n")


main()
