'''
/****************************************************************************************
   LISTA DE PRECIOS
// EN UN NEGOCIO SE CONOCE LA LISTA DE PRECIOS DE 5 PRODUCTOS
//        EL CODIGO (NRO. ENTERO DE 3 cifras)
          PRECIO (real)
// CARGAR LOS DATOS EN VECTORES PARALELOS (CODIGO-PRECIO). .
// MOSTRAR LOS DATOS INGRESADOS
// INDICAR LOS PRODUCTOS MAS CAROS
// SE CONSULTA EL PRECIO, SEGUN EL CODIGO DEL PRODUCTO.
// FIN DE LA CONSULTA CODIGO DE PRODUCTO CERO.
****************************************************************************************/
'''

def LeeControlRango(LI ,LS):
    DATO=int(input("INGRESAR DATO:"))
    while(DATO<LI or DATO > LS):
        DATO=int(input("INGRESAR DATO:"))
    return DATO

def CARGA(VC,VP,NN):
    for I  in range(NN):
        print("\nINGRESAR CODIGO DE PRODUCTO (3 CIFRAS)")
        #VC[I]= LeeControlRango(100,999)
        VC.append(LeeControlRango(100,999))
        print("\nINGRESE PRECIO ")
        #VP[I]=float(input())
        VP.append(float(input("Ingrese un precio")))
  
def CARGA_SIN_DUPLICADOS(VC,VP,NN):
    i=0
    while i < NN:
        print("\nINGRESAR CODIGO DE PRODUCTO (3 CIFRAS)")
        codigo=LeeControlRango(100,999)
        pos=BUSQUEDA(VC,codigo,NN)
        
        if pos == -1:
             VC.append(LeeControlRango(100,999))
             print("\nINGRESE PRECIO ")
             VP.append(float(input("Ingrese un precio")))
             i=i+1
        else:
            print("Error codigo duplicado")
  
def MOSTRAR(VC,VP,NN):
    print("\nCODIGO PRODUCTO          PRECIO ")
    for I in range(NN):
        print("\n " + str(VC[I])+"            "+ str(VP[I]))


def MAXIMO(V,NN):
    MAXI= V[0]
    for I in range(1,NN):
        if (V[I]>MAXI):
            MAXI = V[I]
    return MAXI

def INFO_PRODUCTO_MAS_CARO (VP, VC,PMAX, NN):
    print("\n PRECIO MAS CARO " + str(PMAX))
    print("\n PRODUCTOS MAS CAROS")
    for I in range(NN):
        if (VP[I]== PMAX):
            print("\n  " + str(VC[I]))


def BUSQUEDA(V,DATO,N):
    I=0
    POSI=-1
    while((POSI == -1) and (I<N)):
        if (V[I]==DATO):
            POSI = I
        else:
            I+=1
    return POSI

#------------------------'PRINCIPAL'
N=5
#COD=[0]*N
#PRE=[0.0]*N

CARGA(COD, PRE ,N)

MOSTRAR(COD, PRE , N)

PMAX= MAXIMO(PRE,N)

INFO_PRODUCTO_MAS_CARO (PRE, COD, PMAX, N)

CP=int(input("\n INGRESAR EL CODIGO DE PRODUCTO A CONSULTAR (0 para terminar): "))
while(CP!=0):
    POS = BUSQUEDA(COD,CP,N)
    if (POS >= 0):
        print("\n PRECIO " + str(PRE[POS]))
    else:
        print("\nNO EXISTE EL CODIGO (PRODUCTO)")

    CP=int(input("\n INGRESAR EL CODIGO DE PRODUCTO A CONSULTAR (0 para terminar): "))
   







