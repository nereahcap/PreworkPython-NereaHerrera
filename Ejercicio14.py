#Ejercicio 14: Calculadora de Descuento
#Crea un programa que calcule el precio final de un artículo después de aplicar un descuento del 20%

def calcular_precio_final (precio):
  descuento = precio * 0.20
  total = precio - descuento
  return total

precio_original = float(input("Intrduzca el precio del artículo: "))  
precio_descuento = calcular_precio_final(precio_original)
print(f"El precio con descuento es: ¨{precio_descuento} ")  
