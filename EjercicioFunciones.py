#ingresaValidaNumero es una funcion que
#recibe por parametro
#li= limite inferior
#ls = limite superior
#texto para la salida por consola
#devuelve el valor ingresado Y VALIDADO!!!!

def ingresaValidaNumero (li,ls,texto):
    valor= int(input(texto))
    while valor <li or valor > ls:
        valor= int(input(texto))
    return valor    
    
    
#principal

cont=0
maximaNota = 0
legajoMax = 0

legajo = ingresaValidaNumero(999,9999,"Ingrese legajo - 999 para finalizar ")

while legajo !=999:    
    nota = ingresaValidaNumero(0,10,"Ingrese una nota entre 0 y 10")
    
    cont = cont + 1

    if nota >maximaNota:
        maximaNota = nota
        legajoMax = legajo
    
    legajo = ingresaValidaNumero(999,9999,"Ingrese un legajo 999 para finalizar ")
    
if cont > 0:
    print("La cantidad de alumnos ingresados es " , cont)
    print ("El legajo de nota maxima es ", legajoMax)
else:
    print ("No se ingresaron datos")
    
    
    
    
    
    
    
    
    




