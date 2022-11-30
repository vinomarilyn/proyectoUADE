def sumar (num1,num2):
    resultado=num1+num2
    return resultado

def restar (num1,num2):
    resultado=num1-num2
    return resultado

def multiplicar (num1,num2):
    #multiplicacion con suma sucesivas
    acumulador=0
    contador=0
    while num2 !=0:
        acumulador = acumulador + num1
        num1 = num1 - 1
        
    
    resultado=acumulador
    return resultado

#Comienza programa principal

for i in range(5):
    n1=int(input("Ingrese número 1: "))
    n2=int(input("Ingrese número 2: "))
    resu=sumar(n1,n2)
    print("El resultado de la suma es: ",resu)
    
    resu=restar(n1,n2)
    print("El resultado de la resta es: ",resu)
    



    