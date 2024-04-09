
#Ejercicio 1: Conversor de Temperatura
#Escribe un programa que convierta una temperatura de grados Celsius a grados Fahrenheit. La formula seria: F=C*(9/5)+32

def Celsius_a_Fahrenheit (Celsius):
  return Celsius * (9/5) + 32
Temperatura_Celsius = float(input("Introduzca la temperatura(Celsius) a convertir a grados Fahrenheit: "))
Temperatura_Fahrenheit = Celsius_a_Fahrenheit (Temperatura_Celsius)
print("La temperatura en Fahrenheit es : ",Temperatura_Fahrenheit)

