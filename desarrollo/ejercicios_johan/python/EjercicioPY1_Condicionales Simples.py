nombre = input("¿Cuál es tu nombre?: ")

print("1.Suma 2. Resta 3.Multiplicación 4.División")
op = int(input("¿Qué Operación Aritmética quieres realizar?(número): "))
if op == 1:
    op = "Suma"
if op == 2:
    op = "Resta"
if op == 3:
    op = "Multiplicación"
if op == 4:
    op = "División"

print("¡Hola " + nombre + "!, vamos a realizar una", op)
num1 = float(input("Ingresa un valor: "))
num2 = float(input("Ingresa otro: "))

if op == "Suma":
    result = num1 + num2
if op == "Resta":
    result = num1 - num2
if op == "Multiplicación":
    result = num1 * num2
if op == "División":
    result = num1 / num2

print("El resultado de la", op, "es:", int(result))
