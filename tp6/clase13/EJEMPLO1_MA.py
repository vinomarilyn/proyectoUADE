#EJEMPLO_MA.py
#ver ejemplos de formato de salida
#https://www.delftstack.com/es/howto/python/python-pad-string-with-spaces/

import random

def maximaTemperatura(mTra,cantProv,cantMes):
    band=0
    max=-1
    for i in range(0,cantProv):
        for j in range(0,cantMes):
            if (mTra[i][j]>max or band==0):
                band=1
                max=mTra[i][j]
              
    return max            


def minimaTemperatura(v,cantProv):
    band=0
    min=200
    for i in range(0,cantProv):
        if (v[i]<min or band==0):
            band=1
            min=v[i]
              
    return min            


#-------------------------------------------------------------------
def inicializar(v,ce):
    for i in range(0,ce):       
        v.append(0)
       
    return v    

#-------------------------------------------------------------------

NUM_PROV    =  23
NUM_MES  =  12
#TRA_MAX = [[0]*NUM_MES for i in range(NUM_PROV)]
TRA_MAX = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
PROVINCIA=["SALTA","JUJUY","BSAS","STA CRUZ","CHUBUT","RIO NEGRO","NEUQUEN","MENDOZA","SAN LUIS","CATAMARCA","LA RIOJA","SGO DEL ESTERO","TUCUMAN","FORMOSA","CHACO","CORRIENTES","MISIONES","SANTA FE","TIERRA DEL FUEGO","ENTRE RIOS","CABA","LA PAMPA","SAN JUAN"]
MES =["ENE","FEB","MAR","ABR","MAY","JUN","JUL","AGO","SEP","OCT","NOV","DIC"]
#CARGA DE LA MATRIZ CON VALORES ALEATORIOS
#matriz = [[], [], []] #La matriz es una lista de listas (lista multidimensional)
for i in range(0,NUM_PROV):
    for j in range(0,NUM_MES):
        numero = random.randint(10,50)
        TRA_MAX[i].append(numero)
#Ahora la matriz ya esta cargada

#Vamos a mostrar cómo quedó la matriz
for i in range(0,NUM_PROV):
    fila = ''
    for j in range(0,NUM_MES):
        fila = fila + str(TRA_MAX[i][j]) + '  '
    print(fila)
    
print()
print()

#VAMOS A MEJORAR LA SALIDA INLCUYENDO NOMBRE DE PROVINCIAS y NOMBRE MESES
#Vamos a mostrar cómo quedó la matriz
fila = ' '
fila=fila.rjust(16," ")
for i in range(0,NUM_MES):
    fila=fila + MES[i].rjust(5," ") + "  "
print (fila)


for i in range(0,NUM_PROV):
    fila = ''
              
    fila =fila + PROVINCIA[i].rjust(16," ") + '  '
    #fila =fila + "{0:<16}".format(PROVINCIA[i]) + '  '
    for j in range(0,NUM_MES):
        fila = fila + str(TRA_MAX[i][j]).rjust(5," ") + '  '
    
    print(fila)
    


total=0

#sumo la primera fila
####SUMA  POR FILAS
for i in range(0,NUM_MES):
    total = total + TRA_MAX [0][i]

#sumo la segunda fila
####SUMA  POR FILA
total=0
for i in range(0,NUM_MES):
    total = total + TRA_MAX [1][i]


#PARA SUMAR POR FILA EL TOTAL DE LA MATRIZ
for i  in range(0,NUM_PROV):
    total=0
    for j in range(0,NUM_MES):
        total = total + TRA_MAX[i][j]
    print(f'Fila [{i}] suma total de las temperaturas {total}')

#PARA SUMAR POR COLUMNA EL TOTAL DE LA MATRIZ

for j in range(0,NUM_MES):
    total=0
    for i in range(0,NUM_PROV):
        total = total + TRA_MAX[i][j]
    print(f'MES [{j+1}] suma total de las temperaturas {total}')

#promedio de temperatura de la prov ubicada en la fila 2
total  = 0
for i in range(0,NUM_MES):
    total = total + TRA_MAX[2][i]
promedio  = total / NUM_MES
print(f'\nEl promedio de la temperatura BsAs es {promedio}')


#AHORA CALCULAMOS EL VALOR MAXIMO DE TEMPERATURA , INFORMAR EL MES DONDE SE ENCONTRO

maxima= maximaTemperatura(TRA_MAX,NUM_PROV,NUM_MES)
print("La maxima temperatura fue ->" + str(maxima))


print("Se encontro en los meses :")
mesesMax=[0]*12
for j in range(0,NUM_MES):
    for i in range(0,NUM_PROV):
        if (TRA_MAX[i][j]==maxima):
            mesesMax[j]=1
            
for i in range(0,NUM_MES):
    if (mesesMax[i]!=0):
        print(MES[i])
        
        
        
        
#AHORA SI QUISIERA CONOCER LA TEMPERATURA PROMEDIO POR PROVINCIA Y LUEGO CONOCER
#LA TEMPERATURA PROMEDIO MINIMA Y la/las PROVINCIAS que tuvieron dicha temperatura
vTempxProv=[]

#lo inicializo en 0 para cada provincia
vTemxProv=inicializar(vTempxProv,23)

# con el vector listo ahora sumamos por filas las matriz y la vamos acumulando en las posiciones
# del vector en paralelo
#PARA SUMAR POR FILA EL TOTAL DE LA MATRIZ
for i  in range(0,NUM_PROV):
    total=0
    for j in range(0,NUM_MES):
        total = total + TRA_MAX[i][j]
    vTemxProv[i]=total/NUM_MES
    
#ahora vamos a buscar el minimo en el vector
minTra=minimaTemperatura(vTempxProv,23)
print(f'La temperatura promedio minima encontrada fue {minTra}')

for i  in range(0,NUM_PROV):
    if vTemxProv==minTra :
        print(f'SE ENCONTRO EN LA PROVINCIA {PROVINCIA[i]}')
  
