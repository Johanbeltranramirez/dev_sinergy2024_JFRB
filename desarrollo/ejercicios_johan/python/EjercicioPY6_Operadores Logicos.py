#Conjunción

print("Conjunción (and)")

num1 = int(input("Escribe un número mayor a 2 y menor a 5: "))

if num1 > 2 and num1 < 5:
    print("\n El número ", num1, "cumple con la condición. \n")
else:
    print("\n El número ", num1, " NO cumple con la condición. \n")


#Disyunción
print("Disyunción (or)")

pal = input("Para cumplir con la condición escribe 'SI' o 'YES': ")
pal = pal.lower()

if pal == "si" or pal == "yes":
    print("\n La condición se cumplió correctamente. \n")
else:
    print("\n No se cumplió con la condición. \n")


#Negación
print("Negación (not)")

num1 = int(input("Ingresa un número igual a 5: "))

if not num1 == 5:
    print("\n El número es diferente de cinco y SÍ cumple la condición. \n")
else:
    print("\n El número es igual a cinco y NO cumple con la condición \n")
