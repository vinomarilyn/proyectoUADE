'''
Se procesan los datos de los casi 90 alumnos de un turno de la materia Elementos de Programación.
Por cada alumno se ingresan:
• DNI (entero, mayor que cero y menor que 99.999.999).
• Nota del Parcial 1 (entero, de 0 a 10).
• Nota del Parcial 2 (entero, de 0 a 10).
• Porcentaje de asistencia (real, mayor o igual a cero).

Para finalizar, se ingresa un DNI igual a cero.

Se pide informar con las leyendas aclaratorias y/o títulos:
a. Según los parciales si promocionó, aprobó, reprobó o estuvo ausente (uno o ambos parciales igual
a cero).
b. Listar los alumnos que no cumplen con la asistencia (mayor o igual a 75%).
c. Informar cuántos alumnos que promocionaron NO cumplen en la asistencia.
d. Informar los alumnos que sacaron 10 en el parcial 2.
e. Informar los alumnos con menor asistencia (puede haber varios).
f. Al finalizar, informar el promedio total de notas de cada parcial y de asistencia
'''


def calculoPromedioNota(n1,n2,CE):
    prom=0
    for i in range (CE):
        prom+= (n1[i]+n2[i])/2.
    return (prom/CE)


def calculoPromedioAsistencia(a,CE):
    prom=0
    for i in range (CE):
        prom+= a[i]
    return (prom/CE)

def minimo(V, NN):
    MIN= V[0]
    for i in range(NN):
        if (V[i]<MIN):
            MIN = V[i]

    return (MIN)

def busqueda_secuencial (v, cant, elem):
    i = 0
    pos = -1
    while(i < cant and pos == -1):
        if(v[i] == elem):
            pos = i
        else:
            i=i+1        
    return pos


def cargavectores (Dni,n1,n2,a,n):
    i=0
    CE=0
    
    auxDNI=int(input("\nIngrese un dni (Finaliza con 0): "))
    while(auxDNI<0):
        auxDNI=int(input("\nIngrese un dni (Finaliza con 0): "))
    
    while(i<n and auxDNI!=0):
    
        Dni.append(auxDNI)
        CE=CE+1

        aux1=int(input("\nIngrese la primera nota: "))
        while(aux1<0 or aux1>10):
            aux1=int(input("\nIngrese la primera nota: "))
            
        n1.append( aux1)


        aux2=int(input("\nIngrese la segunda nota: "))
        while(aux2<0 or aux1>10):
            aux2=int(input("\nIngrese la segunda nota: "))
        n2.append( aux2)
       
        auxA=float(input("\nIngrese porcentaje de asistencia: "))
        while(auxA<0 and auxA>100):
            auxA=float(input("\nIngrese porcentaje de asistencia: "))
        a.append( auxA)
       
        

        if(CE<n):
            pos=0
            auxDNI=int(input("\nIngrese un dni (Finaliza con 0): "))
            while(auxDNI<0 or pos!=-1):
                pos=busqueda_secuencial(Dni,i,auxDNI)
                if (pos!=-1):
                    print("\nDNI duplicado.")
                    auxDNI=int(input("\nIngrese un dni (Finaliza con 0): "))    
    return CE



#                   /// PUNTO A

def ListadoA( Dni,  n1,  n2,  CE):

    print("\n\n\n************************* PUNTO A ************************* \n")
    print("\n---- LISTADO DE ALUMNOS SITUACION CURSADA ----\n")
    print("\n---- DNI      \t NOTA 1 \t NOTA 2 \t SITUACION ----\n")

    for i in range(CE):
        if(n1[i] >=7 and n2[i]>=7):
            print(f'\n    {str(Dni[i]).rjust(10," ")} \t   {str(n1[i]).rjust(4," ")}   \t  {str(n2[i]).rjust(4," ")}   \t PROMOCIONO ----\n')
        else:
            if(n1[i] >=4 and n2[i]>=4):
                print(f'\n    {str(Dni[i]).rjust(10," ")} \t   {str(n1[i]).rjust(4," ")}   \t  {str(n2[i]).rjust(4," ")}   \t APROBO ----\n')
            else:
                if(n1[i] >0 and n2[i]>0):
                    print(f'\n    {str(Dni[i]).rjust(10," ")} \t   {str(n1[i]).rjust(4," ")}   \t  {str(n2[i]).rjust(4," ")}   \t REPROBO ----\n')
        
                else:
                    print(f'\n    {str(Dni[i]).rjust(10," ")} \t   {str(n1[i]).rjust(4," ")}   \t  {str(n2[i]).rjust(4," ")}   \t AUSENTE ----\n')
        

# ---------------------   /// PUNTO BC

def ListadoBC( Dni,  n1,  n2, a,  CE):

    cont=0
    contP=0

    print("\n\n\n************************* PUNTO B ************************* \n")
    print("\n---- LISTADO DE ALUMNOS QUE NO CUMPLEN CON EL 75% ASISTENCIA ----\n")
    print("\n---- DNI ----\n")

    for i in range(CE):
        if (a[i]<75):
            print(f'\n    {Dni[i]}')
            cont=cont+1
            

    print("\n--------------------------------------\n")
    print(f'\nTOTAL={cont}\n')
    print("\n--------------------------------------\n")



    print("\n\n\n************************* PUNTO C ************************* \n")
    print("\n---- LISTADO DE ALUMNOS PROMOCIONADOS QUE NO CUMPLEN CON EL 75% ASISTENCIA ----\n")
    print("\n---- DNI ----\n")

    for i in range (CE):
        if(n1[i] >=7 and n2[i]>=7):
            if (a[i]<75):
                print(f'\n    {Dni[i]}')
                contP=contP+1
            

    print("\n--------------------------------------\n")
    print(f'\nTOTAL={contP}\n')
    print("\n--------------------------------------\n")


def ListadoD(Dni,n2,CE):

    print("\n\n\n************************* PUNTO D ************************* \n")
    print("\n---- ALUMNOS CON NOTA 10 EN EL SEGUNDO PARCIAL ----\n")
    print("\n---- DNI  ----\n")

    for i in range(CE):
        if(n2[i]==10):
            print(f'\n    {Dni[i]}')

def ListadoE(Dni,a,menor,CE):

    print("\n\n\n************************* PUNTO E ************************* \n")
    print(f'\n---- ALUMNOS CON ASISTENCIA MENOR = {menor} ----\n')
    print("\n---- DNI  ----\n")

    for i in range (CE):
        if(a[i]==menor):
            print(f'\n    {Dni[i]}')

#-------------------- PROGRAMA PRINCIPAL
MAXIMA_ALUMNOS=90
vDni=[]
vnota1=[]
vnota2=[]
vA=[]
ce=0

ce=cargavectores(vDni,vnota1,vnota2,vA,MAXIMA_ALUMNOS)

if (ce>0):
    ListadoA(vDni,vnota1,vnota2,ce)
    ListadoBC(vDni,vnota1,vnota2,vA,ce)
    ListadoD(vDni,vnota2,ce)

    min=minimo(vA,ce)
    ListadoE(vDni,vA,min,ce)

    promedioNotas = calculoPromedioNota(vnota1,vnota2,ce)
    promedioAsistencia = calculoPromedioAsistencia(vA,ce)

    print("\n\n\n---- PUNTO F ----\n")
    print(f'\n---- NOTA PROMEDIO DE LOS ALUMNOS {promedioNotas} ----\n')
    print(f'\n---- ASISTENCIA PROMEDIO DE LOS ALUMNOS {promedioAsistencia}----\n' )
    print("\n---------------------------\n")
else:
    print("NO SE INGRESARON DATOS")

