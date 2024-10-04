num1, num2 = 0, 1

while num2 <= 1597:
    print(num1, num2, end=" ")
    num1 = num1 + num2
    num2 = num1 + num2

#Ejemplo de break
print("\nWhile con BREAK \n")
contador = 0

while contador < 100:
    contador += 1

    if contador == 5:
        break
    print("Valor actual de la variable:", contador)

print("Fin del programa, la sentencia break ya se ejecutó")

#Ejemplo para continue
print("\n While con CONTINUE \n")
contador = 0

while contador < 100:
    contador += 1

    if contador == 5:
        continue
    print("Valor actual de la variable:", contador)

print("Fin del programa, la sentencia break ya se ejecutó")
