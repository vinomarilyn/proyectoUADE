#Funciones

def CargaDni():
    ingreso=int(input("ingrese DNI del Alumno: "))
    while ingreso<0 or ingreso>99999999:
        ingreso=int(input("Error! Por favor ingrese DNI valido: "))
    return ingreso
        

def CargaParcial(n,li,ls):
    ingreso=int(input(f"\ningrese nota del {n}° parcial: "))
    while ingreso<li or ingreso>ls:
        ingreso=int(input("\n Error! Por favor reingrese la nota del parcial: "))
    return ingreso

def CargaAsist():
    ingreso=float(input("\ningrese porcentaje de asistencia: "))
    while ingreso<0:
        ingreso=float(input("\nError! Por favor reingrese porcentaje de asistencia: "))
    return ingreso
        
    
#---------------------------
#programa principal
dni=[]
notaParcial1=[]
notaParcial2=[]
porcentajeAsistencia=[]
alumnosLibres=[]
contC=0

for i in range (0,3):
    dni.append(CargaDni())
    notaParcial1.append(CargaParcial(1,0,10))
    notaParcial2.append(CargaParcial(2,0,10))
    porcentajeAsistencia.append(CargaAsist())

#i=int(input("seleccione indie de alumno: "))

    if notaParcial1[i]==0 or notaParcial2[i]==0:
        print("\na) Alumno AUSENTE")

    else:
        if notaParcial1[i]<=4 and notaParcial2[i]<=4:
           print("\na) El Alumno REPROBO la materia") 
        else:
            if notaParcial1[i]>=7 and notaParcial2[i]>=7:
                print("\na) El Alumno PROMOCIONO la materia")
            else:
                print("\na) El Alumno APROBO la materia")

    if notaParcial2[i]==10:
        print("\nd) Este Alumno saco 10 en el 2° Parcial")

    if porcentajeAsistencia[i]<=75:
        alumnosLibres.append(dni[i])
        
    if notaParcial1[i]>=7 and notaParcial2[i]>=7 and porcentajeAsistencia[i]<=75:
        contC+=1
    
    #if notaParcial2[i]==10:
        #Aca va la logica del informe del punto d)
    
        
print(f"\nHay un total de {contC} alumnos que promocionaron y no cumplen con la asistencia")
print("\nListado de alumnos libres: ",alumnosLibres)





