def LeeControlRango(li,ls,texto):
    valor=int(input(texto))
    while valor<li or valor >ls:
        valor=int(input("Error,"+ texto))
    return valor

def LeeControlRangoValor(li,ls,cf,texto):
    valor=int(input(texto))
    while (valor<li or valor >ls) and valor !=cf:
        valor=int(input("Error,"+ texto))
    return valor


def cargaLegajos():
    listaLegajos=[]
    listaEscritorios=[]
    
    legajo = LeeControlRangoValor(10000,99999,-1,"Ingrese numero de legajo")
        
    while legajo != -1:
        escritorio = LeeControlRango(1,35,"Ingrese numero de escritorio")
                
        listaLegajos.append(legajo)
        listaEscritorios.append(escritorio)
        
        legajo = LeeControlRangoValor(10000,99999,-1,"Ingrese numero de legajo")
       
    print(listaLegajos)
    print(listaEscritorios)
        
    return listaLegajos,listaEscritorios

def mostrarAlumnos(lista1,lista2):    
    for i in range(len(lista1)):
        print(f"Escritorio={lista2[i]} corresponde al alumno {lista1[i]}")
        
        
def leeMayorCero():
    valor=int(input("Ingrese valor mayor a cero"))
    while valor<= 0:
        valor=int(input("Error- Ingrese valor mayor a cero"))
    return valor

#--------------------------PRINCIPAL
alumnos,escritorios=cargaLegajos()

mostrarAlumnos(alumnos,escritorios)
