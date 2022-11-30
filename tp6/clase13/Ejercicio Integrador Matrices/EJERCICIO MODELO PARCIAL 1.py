
def ingresa_valida(linf,lsup):
    nro=int(input("Ingrese un valor entero"))
    while(nro < linf or nro > lsup):
        nro=int(input("Ingrese un valor entero"))
    return nro

def ingresa_valida2( valor):
    nro=int(input("Ingrese un valor entero"))
    while(nro <= valor):
        nro=int(input("Ingrese un valor entero"))
    return nro


def ingresa_valida_real( valor):
    precio=float(input("Ingrese un precio"))
    while(precio <= valor):
        precio=float(input("Ingrese un precio"))
    return precio

def inicializar_Mat( matriz ,  cf, cc):
  
    for f in range (cf):
        matriz.append([])
        for c in range (cc):
            matriz[f].append(0)

def carga_precios( vec,  cant):
    for i in range (cant):
        print("Ingrese el precio unitario del producto " + str(i+1))
        vec.append(ingresa_valida_real(0))
       
def punto_A( matriz,  cf, cc):
    ##Encabezado de la matriz.
    mensaje=""
   
    print("\n---------------------------------------------------------------------------------------------------------------------\n")
    
    mensaje="Producto\\Mes"

    for c in range (cc):
        mensaje =mensaje + str(c+1).rjust(8," ")
    
    print(mensaje)
    print("\n---------------------------------------------------------------------------------------------------------------------")
    #Recorrido por productos.
    for f in range (cf):
        mensaje=""
        mensaje=mensaje + "\n"+str(f+1).rjust(13," ") 
    
        for c in range (cc):
            mensaje = mensaje +  str(matriz[f][c]).rjust(8," ") 
            
        print(mensaje)
        #print("\n-------------------------------------------------------------------------------\n")
        

def punto_B( matriz, vec, vfact,  cf, cc):
    for f in range (0,cf):
        sum=0
        for c in range (0,cc):            
            sum+=matriz[f][c]
        vfact.append(vec[f] * sum)

def maximo (vfact, tam):
    posMax=0
    max=vfact[posMax]

    for i in range (1,tam):
        if(vfact[i]>max):           
            max=vfact[i]
            posMax=i
    
    return posMax


def minimo ( vfact, tam):
    posmin=0
    min=vfact[posmin]

    for i in range(tam):    
        if(vfact[i]<min):
            min=vfact[i]
            posmin=i
    return posmin

def punto_C ( matriz, vprecio,  cf , cc):
    vecfactrim=[0.0]*4 
    
    '''POSICIÓN CONTENIDO
              0      Facturación del 1er trimestre.
              1      Facturación del 2do trimestre.
              2      Facturación del 3er trimestre.
              3      Facturación del 4to trimestre.'''
                            
    for f in range (cf):
        for c in range (cc):
             # c/3= > Retorna el número entero de la división.
                     # si c<3 -> índice del primer trimestre,
                     # si c<6 ->índice del 2do trimestre,
                     # c<9 ->índice del 3er trimestre,
                     # c <12 -> índice del 4º trimestre.
             
            vecfactrim[c//3]+=matriz[f][c] * vprecio[f]
        

    posmin=minimo(vecfactrim,4)
    print("\n El trimestre de menor facturacion fue " +str(posmin+1)+"  con una facturacion de " + str(vecfactrim[posmin]))
# -----------------------PROGRAMA PRINCIPAL
FILAS=20
COLS=12

'''
mat=[] #creo una lista vacia

vecprecio=[]
vecfact=[]

inicializar_Mat(mat,FILAS,COLS)
carga_precios(vecprecio,FILAS)

print("Ingrese el codigo de producto (1-20, 0 para finalizar)")
cod=ingresa_valida(0, FILAS)

while(cod !=0):

    print("Ingrese dia (1-31):")
    dia=ingresa_valida(0 + 1,31)
    print("Ingrese mes (1-12):")
    mes=ingresa_valida(0 + 1,COLS)
    print("Ingrese cantidad de unidades vendidas (numero entero Mayor a cero):")
    cantunid = ingresa_valida2(0)

    mat[cod-1][mes-1]+=cantunid

    print("Ingrese el codigo de producto (1-20, 0 para finalizar)")
    cod=ingresa_valida(0,FILAS)

'''
vecfact=[]
vecprecio=[150,170,50,30,20,100,500,400,650,780,960,205,220,300,180,90,200,340,600,500]
mat=[[0,0,0,0,0,0,0,78,20,0,0,0],
     [0,0,0,0,0,0,0,0,150,0,0,0],
     [0,0,0,0,0,0,0,0,200,0,0,0],
     [45,0,0,1000,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,35,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,34,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,20,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,40,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,100,0,0,0,0,80,50,0],
     [0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,30],
     [0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,20,0,0,0,0,0,0,0]     
    ]


punto_A(mat,FILAS,COLS)

punto_B(mat,vecprecio,vecfact,FILAS,COLS)

print(vecfact)  

posmax=maximo(vecfact,FILAS)
print("\nEl producto de mayor facturacion es :" + str(posmax+1)+ " con una facturacion de $" + str(vecfact[posmax]))

punto_C(mat,vecprecio,FILAS,COLS)

