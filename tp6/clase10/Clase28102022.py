#cargar una lista con valores numericos
#entre 1 y 100- CF numero igual 0

#1 mostrar la lista cargada
#2 calcular la suma de los elementos
#3 calcular el valor maximo e informar su posicion
#4 calcular el valor minimo dentro de la lista

def ingresaValidaNumero(li,ls):
    nro=int(input(f"Ingrese un numero entre {li} y {ls}"))
    while nro<li or nro>ls:
        nro=int(input(f"Error - Ingrese un numero ente {li} y {ls}"))
    return nro    

def cargar(li):
   
   num=ingresaValidaNumero(0,100)
   
   while num!= 0:       
       li.append(num)       
       num=ingresaValidaNumero(0,100)
    
       
def mostrarLista(li):
    print("Listado de numeros ingresados")
    for i in range (len(li)):
        print(li[i])
       
       
def sumar(li):
    suma=0
    
    for i in range(len(li)):
        suma+=li[i]
    
    return suma
          

def maximo1(li):
        
    maximo = li[0]
    
    for i in range (1,len(li)):
        if li[i]>maximo:
            maximo=li[i]
    
    return maximo
        

def maximo2(li):
        
    maximo = li[0]
    indice=0
    
    for i in range (1,len(li)):
        if li[i]>maximo:
            maximo=li[i]
            indice=i
            
    return indice
        
        
def minimo1(li):
        
    minimo = li[0]
    
    for i in range (1,len(li)):
        if li[i]<minimo:
            minimo=li[i]
    
    return minimo      
        
def listarMinimos(li,valMin):
    
    print("Posiciones donde encontramos valores minimos")
    for i in range (len(li)):
        if li[i] == valMin:
            print(i+1)
            
# ----- principal
lista=[]

cargar(lista)
    
print(lista)

mostrarLista(lista)

sumaDeLista=sumar(lista)

promedio =sumaDeLista/len(lista)

print("La suma de los elementos es ",sumaDeLista)
print("El promedio es ", promedio)

#calculo del valor MAXIMO

if len(lista) > 0:
    valorMaximo = maximo1(lista)
    print ("El valor maximo de la lista es: ", valorMaximo)
    indiceMaximo = maximo2(lista)    
    print ("Se encuentra en el indice :", indiceMaximo)
    
    valorMinimo =minimo1(lista)
    listarMinimos(lista,valorMinimo)
    
    
    
else:
    print("Lista vacia")










    
    
    
    



