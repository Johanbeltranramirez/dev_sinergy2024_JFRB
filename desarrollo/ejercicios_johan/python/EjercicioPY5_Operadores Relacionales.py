print("Introduce dos números a comparar: \n")

num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

print("\n Los números a compara son: ", num1," y ", num2, "\n")

if num1 == num2:
    print("Es igual...")
if num1 != num2:
    print("Es diferente...")
if num1 < num2:
    print("Es menor...")
if num1 > num2:
    print("Es mayor...")
if num1 <= num2:
    print("Es menor o igual...")
if num1 >= num2:
    print("Es mayor o igual...")
