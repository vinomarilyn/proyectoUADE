contVtasTotal =0
contVtas10Dto = 0
contSDto = 0
cantTotal = 0
vtasTotal=0
vtasSDto=0
vtas10Dto =0

contVtasTotal=0
contVtas10Dto=0

cantidad = int(input("ingrese cantidad: "))
while cantidad <=0 and cantidad !=-1:
    cantidad = int(input("ingrese cantidad: "))
while cantidad !=-1:
    precioBase = int(input("ingrese precio base: "))
    precioTotal = cantidad * precioBase
    contVtasTotal = contVtasTotal+1
    print(precioTotal)
    if cantidad > 100:
        precioTotal = precioTotal *0,75 ##como puedo multiplicar con numeros con coma
        print(precioTotal)
    else:
        if cantidad >12 and cantidad <=100:
            precioTotal = precioTotal *0,90
            contVtas10Dto = contVtas10Dto +1
            vtas10Dto = vtas10Dto + precioTotal
        else:
            contSDto = contSDto+1
            vtasSDto = vtasSDto+precioTotal
    vtasTotal = vtasTotal + precioTotal
    cantTotal = cantTotal +cantidad
    cantidad = int(input("ingrese cantidad: "))
    while cantidad <=0 and cantidad !=-1:
        cantidad = int(input("ingrese cantidad: "))
if cantidad >0:
    promedio = vtasTotal / cantTotal
    print("promedio: ", promedio)
    print("ventas total: ",vtasTotal)
    print("contador de ventas totales ", contVtasTotal)
    print("ventas 10% de descuento: ",vtas10Dto)
    print("contador de ventas del %10 de descuento ", contVtas10Dto)
    print("ventas de descuento: ",vtasSDto)
    print("contador de ventas de descuento ", contSDto)
else:
    print("No se realizaron ventas")
