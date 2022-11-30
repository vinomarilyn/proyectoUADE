def LeeControlRango(li,ls,texto):
    valor=int(input(texto))
    while valor<li or valor >ls:
        valor=int(input("Error,"+ texto))
    return valor

def cargaLegajos(ce):
    lista=[0]*ce
    
    for i in range(ce):
        escritorio = LeeControlRango(1,35,"Ingrese numero de escritorio")
        legajo = LeeControlRango(10000,99999,"Ingrese numero de legajo")
        
        lista[escritorio-1]=legajo
        
    return lista

def mostrarAlumnos(lista,ce):    
    for i in range(ce):
        print(f"Escritorio={i+1} corresponde al alumno {lista[i]}")
        
        
def leeMayorCero():
    valor=int(input("Ingrese valor mayor a cero"))
    while valor<= 0:
        valor=int(input("Error- Ingrese valor mayor a cero"))
    return valor

#--------------------------PRINCIPAL
alumnos=cargaLegajos(3)

mostrarAlumnos(alumnos,3)

