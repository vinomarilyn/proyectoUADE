def sumar (num1,num2):
    resultado=num1+num2
    return resultado

def restar (num1,num2):
    resultado=num1-num2
    return resultado

#Comienza programa principal

for i in range(5):
    n1=int(input("Ingrese número 1: "))
    n2=int(input("Ingrese número 2: "))
    resu=sumar(n1,n2)
    print("El resultado de la suma es: ",resu)
    
    resu=restar(n1,n2)
    print("El resultado de la resta es: ",resu)
    
    







    