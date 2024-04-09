#Ejercicio 8: Cálculo del Índice de Masa Corporal (IMC)
#Escribe un programa que calcule el Índice de Masa Corporal (IMC) de una persona.

peso = float(input("Ingrese su peso en kilogramos: "))  

altura = float(input("Ingrese su altura en metros: "))  

imc = peso / (altura ** 2)  

print("Su índice de masa corporal (IMC) es:", imc)  
