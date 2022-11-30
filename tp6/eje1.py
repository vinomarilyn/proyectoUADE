##Ejercicio 1: Diseñar una función que reciba dos parámetros numéricos enteros, calcule y devuelva el
##resultado de la multiplicación de ambos utilizando sólo sumas.
##Desarrollar un programa principal para crear la siguiente serie numérica de N términos,
##comienza en uno y cada siguiente término se obtiene multiplicando el anterior por la ubicación:

##1 2 6 24 120
##*2 *3 *4 *5
def multiplicacion(num1,num2):
    cont=0
    while 0 != num1 and 0 != num2:
        resultado=num1*num2
        return resultado
        
#comienza programa principal
n1=int(input("ingrese numero 1: "))
n2=int(input("ingrese numero 2: "))  
while 0 != n1 and 0 != n2:

    resu=multiplicacion(n1,n2)
    print("el resultado es: ", resu)
    
    