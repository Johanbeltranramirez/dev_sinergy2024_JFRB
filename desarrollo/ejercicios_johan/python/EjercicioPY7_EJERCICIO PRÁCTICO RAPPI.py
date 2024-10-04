print("Sistema que Determina los días de Vacaciones por departamento \n")

nomEmp = input("Ingrese el nombre completo del empleado: ")
genEmp = input("¿Cuál es el género del empleado?(Mujer/Hombre): ")
clvDep = int(input("Ingrese la clave dada por departamento: "))
ansAnt = int(input("Ingresar Antiguedad del empleado en la compañía(AÑOS ENTEROS): "))

if clvDep == 1:

    if ansAnt == 1:
        diasVac = 6
    elif ansAnt >= 2 and ansAnt<= 6:
        diasVac = 14
    elif ansAnt > 7:
        diasVac = 20
    else:
        print("CERO")

elif clvDep == 2:
    
    if ansAnt == 1:
        diasVac = 7
    elif ansAnt >= 2 and ansAnt<= 6:
        diasVac = 15
    elif ansAnt > 7:
        diasVac = 22
    else:
        print("El empleado no tiene derecho a vacaciones")

elif clvDep == 3:
    
    if ansAnt == 1:
        diasVac = 10
    elif ansAnt >= 2 and ansAnt<= 6:
        diasVac = 20
    elif ansAnt > 7:
        diasVac = 30
    else:
        print("El empleado no tiene derecho a vacaciones")

else:
    print("La clave ingresada no existe")

genEmp = genEmp.lower()

if genEmp == "mujer":
    trat = "La colaboradora"
elif genEmp == "hombre":
    trat = "El colaborador"
else:
    print("Género Inválido")
    
print("\n", trat, nomEmp, "tiene derecho a", diasVac, "días de vacaciones")

        
