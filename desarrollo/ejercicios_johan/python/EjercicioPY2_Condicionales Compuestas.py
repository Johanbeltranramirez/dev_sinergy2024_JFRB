print("Sistema para calcular el promedio de un alumno")

nom = input("Para empezar, ¿Cuál es tu nombre? ")

math = float(input(nom + ", ¿Cuál es tu calificación en matematicas?: "))
quim = float(input(nom + ", ¿Cuál es tu calificación en química?: "))
espñol = float(input(nom + ", ¿Cuál es tu calificación en español?: "))

prom = (math + quim + espñol) / 3

if prom >= 6:
    print("!Felicidades¡", nom, "APROBASTE con un promedio de", round(prom,1))

else:
    print("Lo sentimos,", nom, "REPROBASTE con un promedio de", round(prom,1))
    
print("CHAU")
