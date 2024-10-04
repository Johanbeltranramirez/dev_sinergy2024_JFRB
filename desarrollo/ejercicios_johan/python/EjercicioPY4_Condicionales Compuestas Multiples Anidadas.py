print("Menú de Opciones \n")
print("Presiona 1 para convertir de número a palabra")
print("Presiona 2 para convertir de palabra a número \n")

op = int(input("¿Cuál es tu opción deseada?:"))

if op == 1:
    print("\n Conversor de número a palabra \n")
    op1 = int(input("¿Cúal es el número que deseas convertir a palabra?: "))

    if op1 == 1:
        print("El número es UNO")
    elif op1 == 2:
        print("El número es DOS")
    elif op1 == 3:
        print("El número es TRES")
    elif op1 == 4:
        print("El número es CUATRO")
    elif op1 == 5:
        print("El número es CINCO")
    else:
        print("El número seleccionado no está registrado")
        
elif op == 2:
    print("\n Conversor de palabra a número \n")

    op2 = input("¿Cúal es la palabra que deseas convertir a número?: ")
    op2 = op2.lower()

    if op2 == "uno":
        print("El número es 1")
    elif op2 == "dos":
        print("El número es 2")
    elif op2 == "tres":
        print("El número es 3")
    elif op2 == "cuatro":
        print("El número es 4")
    elif op2 == "cinco":
        print("El número es 5")
    else:
        print("El número seleccionado no está registrado")
else:
    print("¡Opción no disponible!")
