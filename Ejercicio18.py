#Ejercicio 18: Contador de Palabras
#Crea un programa que cuente la cantidad de palabras en una oración ingresada por el usuario.

def contador_palabras (frase):
  palabras = frase.split ()
  cantidad_palabras = len (palabras)
  return cantidad_palabras

oracion = input ("Introduce una oración: ")
numero_palabras = contador_palabras(oracion)
print(f"La oración tiene {numero_palabras} palabras")
 
