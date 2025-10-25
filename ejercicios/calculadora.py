print("------------------------------------")
print("CALCULADORA EN PYTHON")
print("------------------------------------")

print("""Las operaciones que puede realizar esta calculadora son:
1. SUMA
2. RESTA
3. MULTIPLICACION
4. DIVISION
5. POTENCIACION
""")

operacion=int(input("Selecciona la operacion que deseas realizar (1, 2, 3, 4, 5): "))
if operacion > 5:
    print("Haz seleccionado una operacion incorrecta")

else:
    if operacion == 1:
        print(f"Haz seleccionado la opcion SUMA")
        num1=int(input("Primer numero: "))
        num2=int(input("Segundo numero: "))
        suma=num1+num2
        print("------------------------------------")
        print(f"{num1} + {num2} = {suma}")
        print("------------------------------------")

    elif operacion == 2:
        print(f"Haz seleccionado la opcion RESTA")
        num1=int(input("Primer numero: "))
        num2=int(input("Segundo numero: "))
        resta=num1-num2
        print("------------------------------------")
        print(f"{num1} - {num2} = {resta}")
        print("------------------------------------")

    elif operacion == 3:
        print(f"Haz seleccionado la opcion MULTIPLICACION")
        num1=int(input("Primer numero: "))
        num2=int(input("Segundo numero: "))
        mult=num1*num2
        print("------------------------------------")
        print(f"{num1} * {num2} = {mult}")
        print("------------------------------------")

    elif operacion == 4:
        print(f"Haz seleccionado la opcion DIVISION")
        num1=int(input("Primer numero: "))
        num2=int(input("Segundo numero: "))
        div=num1/num2
        print("------------------------------------")
        print(f"{num1} / {num2} = {div}")
        print("------------------------------------")

    elif operacion == 5:
        print(f"Haz seleccionado la opcion POTENCIACION")
        num1=int(input("Primer numero: "))
        num2=int(input("Segundo numero (sera el exponente): "))
        poten=num1**num2
        print("------------------------------------")
        print(f"{num1} elevado a la {num2} = {poten}")
        print("------------------------------------")

print("------------------------------------")
print("SE HA COMPLETADO LA EJECUCION DEL PROGRAMA")
print("------------------------------------")




    

    


        





