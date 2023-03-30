print("Bienvenidos a este programa")

print("En este programa se tomaran 3 numeros enteros: ")

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))

if num2 < num1 > num3:
    print("El numero mayor es el primer numero, el cual es:", num1)
elif num1 < num2 > num3: 
    print("El numero mayor es el segundo numero, el cual es:", num2)
elif num1 < num3 > num2: 
    print("El numero mayor es el tercer numero, el cual es:", num3)
else: 
    print("Todos los numeros son iguales")

if num2 > num1 < num3:
    print("El numero menor es el primer numero, el cual es:", num1)
elif num1 > num2 < num3: 
    print("El numero menos es el segundo numero, el cual es:", num2)
elif num1 > num3 < num2: 
    print("El numero menor es el tercer numero, el cual es:", num3)
else: 
    print("Todos los numeros son iguales")
    
print("Fin del programa")