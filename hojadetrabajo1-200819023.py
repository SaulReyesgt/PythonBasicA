#Marvin Saul Reyes Molina
#200819023
#Ejercicio 1
n = int(input("Ingrese un número entero para el ejercicio 1: "))
for i in range(n):
    for j in range(i+1):
        print("*", end="")
    print("")


#Ejercicio 2

n = int(input("Introduce un número entero para el ejercicio 2 (recuerda que debe ser mayor o igual que 2): "))
i = 2
while n % i != 0:
    i += 1
if i == n:
    print(str(n) + " es primo")
else:
    print(str(n) + " no es primo")
