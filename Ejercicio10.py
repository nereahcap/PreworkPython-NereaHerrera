#Ejercicio 10: Determinar el Día de la Semana
#Escribe un programa que determine el día de la semana correspondiente a un número ingresado por el usuario (1 para lunes, 2 para martes, etc.).

def determina_dia(numero):
  dias_semana= ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
  if numero>=1 and numero<=7:
    return dias_semana[numero-1]
  
numero=int(input("Introduce un númmero del 1 al 7:"))
nombre_dia= determina_dia(numero)
print(f"El día de la semana correspondiente al número introducido es: {nombre_dia}")

