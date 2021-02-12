#Marvin Saul Reuyes Molina 200819023
#Hoja de trabajo 2

#Ejercicio 1

clave = "contraseña"
contraseña = input("Introduce la contraseña: ")
if clave == contraseña.lower():
    print("La contaseña coincide")
else:
    print("La contraseña no coincide")

#Ejercicio 1 - 2

clave = input("Introduzca una contraseña: ")
contraseña = input("Introduzca nuevamente la contraseña: ")
if clave.lower() == contraseña.lower():
    print("La contaseña coincide")
else:
    print("La contraseña no coincide")




# Ejercicio 2

nombre = input("¿Cómo se llama? ")
genero = input("¿Cuál es su genero (M o F)? ") #M MASCULINO F = FEMENINO
if genero == "F":
    if nombre.lower() < "m":
        grupo = "A"
    else:
        grupo = "B"
else:
    if nombre.lower() > "n":
        grupo = "A"
    else:
        grupo = "B"
print("Su grupo es " + grupo)