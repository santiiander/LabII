def cargar_vector():
    longitud = int(input("Ingrese la longitud del vector: "))
    vector = [] * longitud
    for i in range(longitud):
        vector.append(input("Ingrese una edad: "))
    return vector

def mostrar_vector(vector):
    for i in range(len(vector)):
        print(vector[i])

def sumatoria(vector):
    suma = 0
    for i in range(len(vector)):
        suma += vector[i]
        return suma

def promedio(suma, vector):
    promEdad = suma / len(vector)
    return promEdad

def mayores_del_prom(promEdad, vector):
    mayor = []
    for i in vector:
        if vector[i] > promEdad:
            mayor.append(vector[i])
    print(mayor)

def edad_mayor_num(vector):
    edadMayor = 0
    for i in range(len(vector)):
        if vector[i] > edadMayor:
            edadMayor = vector[i]
            return edadMayor
    print(edadMayor)

def edad_mayor_letras(edadMayor):
    unidades = ['', 'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve']
    decenas = ['', 'diez', 'veinte', 'treinta', 'cuarenta', 'cincuenta', 'sesenta', 'setenta', 'ochenta', 'noventa']
    especiales = ['once', 'doce', 'trece', 'catorce', 'quince', 'dieciséis', 'diecisiete', 'dieciocho', 'diecinueve']
    
    if edadMayor < 10:
        return unidades[edadMayor]
    elif edadMayor < 20:
        return especiales[edadMayor-11]
    elif edadMayor < 100:
        if edadMayor % 10 == 0:
            return decenas[edadMayor//10]
        else:
            return decenas[edadMayor//10] + ' y ' + unidades[edadMayor%10]

def ordenar_edades(vector):
    vector.sort()

def diferencia_edad(vector, promEdad):
    for i in vector:
        print(promEdad, " - ", vector[i], " = ", (promEdad-vector[i]))

def menu():
    variable = True
    while variable:
        print("Bienvenid@")
        print("¿Qué desea hacer?")
        print("1- Cargar el vector.")
        print("2- Mostrar el vector.")
        print("3- Sumar las edades.")
        print("4- Calcular el promedio de las edades.")
        print("5- Mostrar las edades mayores al promedio.")
        print("6- Mostrar la edad más alta (en número).")
        print("7- Mostrar la edad más alta (en letras)")
        print("8- Ordenar el vector.")
        print("9- Mostrar la diferencia de las edades.")
        seleccion = int(input("Ingrese la opción deseada (0 para salir): "))
        if seleccion == 1:
            cargar_vector()
        if seleccion == 2:
            mostrar_vector()
        if seleccion == 3:
            sumatoria()
        if seleccion == 4:
            promedio()
        if seleccion == 5:
            mayores_del_prom()
        if seleccion == 6:
            edad_mayor_num()
        if seleccion == 7:
            edad_mayor_letras()
        if seleccion == 8:
            ordenar_edades
        if seleccion == 9:
            diferencia_edad()
        if seleccion == 0:
            variable = False

menu()