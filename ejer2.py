contAprobados= 0
contDesaprobados= 0
aplazos=0
legajo = int(input("ingrese su legajo: "))
while legajo !=-1:
    nota = int(input("ingrese su nota: "))
    while nota<1 or nota>10:
        nota = int(input("ingrese su nota: "))
        
    if nota>=1 and nota < 4:
        contDesaprobados= contDesaprobados + 1
        if nota ==1:
            aplazos = aplazos +1
    else:
        contAprobados= contAprobados + 1
    legajo = int(input("ingrese su legajo: "))
print("La cantidad de personas aprobadas:", contAprobados)
print("La cantidad de personas desaprobadas:", contDesaprobados)

if contDesaprobados > 0:
    porcentajeAplazados= aplazos/contDesaprobados
    
    promMenor18= sumaMen18/contMen18
    print("Porcentaje de alumnos que tienen 1:", porcentajeAplazados)
    