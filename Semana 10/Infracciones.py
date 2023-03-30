print("BIENVENIDO/A A NUESTRO PROGRAMA")

infracciones = int(input("Ingrese el numero de infracciones de este mes: "))

infracciones_diarias = infracciones / 30 

prom_matutino = infracciones * 0.2 

print("El promedio de infracciones de la mañana es de: ", prom_matutino)

prom_vespertino = infracciones * 0.35

print("El promedio de infracciones de la tarde es de: ", prom_vespertino) 

prom_nocturno = infracciones * 0.45

print("El promedio de infracciones nocturnas es de: ", prom_nocturno)

print("Fin del programa")