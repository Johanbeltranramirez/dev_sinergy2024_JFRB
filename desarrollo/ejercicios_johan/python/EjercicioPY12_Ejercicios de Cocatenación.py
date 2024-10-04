#Función Len()

print("Gracias tiene", len("Gracias"), "caracteres")

#Cocatenación con método format()

nom = "Johan"
edad = 12

print("¿Cómo estás?, {}. Tienes {} años de edad.".format(nom, edad)) 


#Cocatenación con f-strings

nom = input("\nEscriba su nombre: ")
print(f"¡{nom} vamos a realizar una suma! \n")

num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))

print(f"{nom}, el resultado de la suma entre {num1} y {num2} es: {num1+num2}")
