#Ejercicio 7: Calculadora Simple
#Crea un programa que realice operaciones aritméticas simples (suma, resta, multiplicación, división) según la elección del usuario

numero1 = int (input("Introduzca el primer número: "))
numero2 = int (input("Introduzca el segundo número: "))

eleccion = 0


while eleccion !=6:
  print ("""
         Indique la operación a realizar:

         1)Suma
         2)Resta
         3)Multiplicar
         4)Dividir
         5)Cambiar números introducidos
         6)Salir de la calculadora
  """)
  eleccion = int (input()) 

  if eleccion == 1:
    print(" ")
    print ("RESULTADO: ", numero1, "+ ",numero2,"=", numero1+numero2 )
  elif eleccion ==2:
    print (" ")
    print ("RESULTADO: ", numero1,"-" , numero2, "=", numero1-numero2)
  elif eleccion ==3:
    print ("")
    print("RESULTADO:", numero1, "x", numero2, "=", numero1 * numero2 )
  elif eleccion ==4:
    print ("")
    print("RESULTADO: ", numero1, "/", numero2, "=", numero1/numero2)
  elif eleccion ==5:
    print ("")
    numero1 = int (input("Introduzca el primer número: "))
    numero2 = int (input("Introduzca el segundo número: "))
  elif eleccion ==6:
    print ("HASTA PRONTO")


