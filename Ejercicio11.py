#Ejercicio 11: Calculadora de Edad
#Escribe un programa que solicite al usuario su año de nacimiento y calcule su edad actual.
def calculadora_edad (anio_nacimiento):
  anio_actual =2024
  edad = anio_actual - anio_nacimiento
  return edad

anio_nacimiento = int (input("Introduce tu año de nacimiento: "))

edad =calculadora_edad(anio_nacimiento)

print (f"Tienes ¨{edad} años")