contMay18=0
sumaMas18=0
contMen18=0
sumaMen18=0
edad = int(input("ingrese una edad: "))
while (edad <0 or edad >100) and edad !=999:
    edad = int(input("ingrese una edad"))
while edad !=999:
    if edad >=18:
        contMay18= contMay18 +1
        sumaMas18= sumaMas18 +edad
    else:
        contMen18= contMen18 +1
        sumaMen18= sumaMen18 +edad
    edad = int(input("ingrese una edad"))
    while (edad <0 or edad >100) and edad !=999:
        edad = int(input("ingrese una edad"))
if contMen18>0:
    promMenor18= sumaMen18/contMen18
    print("el promedio de menores es: ", promMenor18)
    print("el contador de menores es: ", contMen18)
else:
    print("No se ingresaron menores a 18 anios")
    
if contMay18>0:
    promMay18= sumaMas18/contMay18
    print("el promedio de mayores es: ", promMay18)
    print("el contador de mayores es: ", contMay18)
else:
    print("No se ingresaron mayores a 18 anios")
    
    
    
    
      
        
    