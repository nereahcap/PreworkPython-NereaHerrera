#Ejercicio 4: Contador de Vocales
#Crea un programa que cuente el número de vocales en una palabra ingresada por el usuario.

cadena = input("Ingrese una cadena de texto: ")  
cadena = cadena.lower()  
contador_vocales = 0  
for caracter in cadena:
    if caracter in "aeiou":
        contador_vocales += 1

print("El número de vocales en la cadena es:", contador_vocales)  
