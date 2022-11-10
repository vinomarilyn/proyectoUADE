'''
Una empresa desea registrar las ventas realizadas de cada uno de sus productos al
finalizar el mes.
Los productos están identificados por un código numérico de 3 cifras. 

Como primera información se ingresa el código y el precio unitario de cada uno de los productos.
Esta carga finaliza con el ingreso de un codigo 99

Luego por cada venta se ingresa:
• Código de producto
• Cantidad de unidades vendidas

El ingreso de datos de las ventas finaliza con un código de producto igual a 0. 

Informar:

• a. El detalle de unidades vendidas de cada producto 
• b. Los productos que mas se vendieron (máxima recaudación)
• c. Listado ordenado en forma ascendente conteniendo lo siguiente:

LISTADO DE UNIDADES VENDIDAS
CODIGO			FACTURACION
XXX				  XXXXX
XXX				  XXXXX
….				…..
XXX				  XXXXXX
		TOTAL FACTURACION :$ XXXXXX
'''

def ingresa_Valida_Rango_Numero(linf,lsup,num):
    
    nro=int(input("Ingrese numero"))
  
    while((nro < linf or nro > lsup) and nro != num):
        nro=int(input("Error, Re-Ingrese numero"))
  
    return nro


def ingresa_valida(linf,lsup):
    nro=int(input("Ingrese numero"))
  
    while(nro < linf or nro > lsup):
        nro=int(input("Error, Re-Ingrese numero"))
  
    return nro


def ingresa_valida2(valor):
    nro=int(input("Ingrese numero"))
  
    while(nro <= valor):
        nro=int(input("Error - Re Ingrese numero"))
  
    return nro
 
def ingresa_valida_float(valor):

    precio=float(input("Ingrese numero"))
  
    while(precio <= valor):
        precio=int(input("Error - Re-Ingrese numero"))
  
    return precio


def buscarCodigo(lista,buscado):
    i=0
    pos=-1
    
    while i < len(lista) and pos ==-1:
        if lista[i] == buscado:
            pos = i
        else:
            i+=1
    
    return pos



def carga_inicial():
    '''Como primera información se ingresa el código y el precio unitario de cada uno de los productos.
    Esta carga finaliza con el ingreso de un precio -1'''
    
    codigos=[]
    precios=[]
    i=0
    
    print(f'Ingrese el codigo del producto(3 digitos) --> 99 para finalizar:')
    cod=ingresa_valida(99,999)
    
    while cod !=99:
        
        #busco si el codigo esta duplicado en la lista
        
        pos=buscarCodigo(codigos,cod)
        
        if pos ==-1:
            #quiere decir que no lo encuentre
            print(f'Ingrese el precio del producto:')

            importe= ingresa_valida_float(0)
            
            codigos.append(cod)
            precios.append(importe)
            
        else:
            print("ERROR codigo duplicado. Reingrese otro codigo")
            
        print('Ingrese el codigo del producto(3 digitos) --> 99 para finalizar:')
        cod=ingresa_valida(99,999)
    
    return codigos,precios
        
        
def cargarVentas(listaCod,listaPrec):
    '''Luego por cada venta se ingresa:
    • Código de producto
    • Cantidad de unidades vendidas

    El ingreso de datos de las ventas finaliza con un código de producto igual a 0. 
    '''
    cantidades=[0] * len(listaCod)
    facturaciones=[0] * len(listaPrec)
    
    print ("COMIENZA EL PROCESO DE CARGA DE VENTAS...")
    
    print("Ingrese un codigo - 0 para finalizar") 
    cod = ingresa_Valida_Rango_Numero(100,999,0)
    
    while cod !=0:
        
        pos = buscarCodigo(listaCod,cod)
        
        if pos !=-1:
            print("Ingrese la cantidad vendida:") 
            cant =ingresa_valida2(0)
            cantidades[pos] += cant
            facturaciones[pos]+=cant*listaPrec[pos]
        else:
            print("ERROR - EL PRODUCTO NO EXISTE")
        print("Ingrese un codigo - 0 para finalizar") 
        cod = ingresa_Valida_Rango_Numero(100,999,0)
    
    return cantidades, facturaciones
      
      
def listadoCantidad(lcod,lcant):
    
    print("---- Detalle de unidades vendidas de cada producto ----") 
    for i in range(len(lcod)):
        print(str(lcod[i]) + "        " + str(lcant[i]))
    
        
def maximo (importes):
    
    maxi=importes[0]

    for i in range (1,len(importes)):
        if(importes[i]>maxi):
            maxi=importes[i]
               
    return maxi

def mostrarIgualA(lC,lF,valor):
        
    print("LISTADO DE PRODUCTOS CON RECAUDACION MAXIMA")
    for i in range (len(lC)):
        if lF[i]==valor:
            print(lC[i])
    

def ordenar(lC,lF):
    for i in range(0, len(lF)-1):
        for j in range(i+1, len(lF)):
            if (lF[j] < lF[i]):
                aux = lF[j]
                lF[j] = lF[i]
                lF[i] = aux
                
                aux2 = lC[j]
                lC[j] = lC[i]
                lC[i] = aux2
    
    
def listado(lC,lF):
    total = 0
    print("LISTADO DE UNIDADES VENDIDAS")
    print("CODIGO			FACTURACION")
    
    for i in range(len(lC)):
        print(lC[i], end="			")
        print(lF[i])
        total += lF[i]
    
    print("-----------------------------")
    print("      TOTAL FACTURADO $" , total)
    
#-------------------------------PRINCIPAL

listaCodigos,listaPrecios = carga_inicial()

print(listaCodigos)
print(listaPrecios)

listaCantidades,listaFacturacion = cargarVentas(listaCodigos,listaPrecios)
print(listaCantidades)
print(listaFacturacion)

if len(listaCantidades)> 0:
    #El detalle de unidades vendidas de cada producto
    listadoCantidad(listaCodigos,listaCantidades)

    # Los productos que mas se vendieron (máxima recaudación)
    maximaRecaudacion = maximo(listaFacturacion)
    mostrarIgualA(listaCodigos,listaFacturacion,maximaRecaudacion)
    
    #• c. Listado ordenado en forma ascendente por importe facturado conteniendo lo siguiente:

    '''
    LISTADO DE UNIDADES VENDIDAS
    CODIGO			FACTURACION
    XXX				  XXXXX
    XXX				  XXXXX
    ….				…..
    XXX				  XXXXXX
            TOTAL FACTURACION :$ XXXXXX
    '''
    ordenar(listaCodigos,listaFacturacion)
    listado(listaCodigos,listaFacturacion)