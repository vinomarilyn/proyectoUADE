def cargarLista(lista):
    valor=int(input("ingrese un numero: "))
    while valor!=0 and valor!=-1:
        lista.append(valor)
        valor=int(input("ingrese un numero: "))
        
    return lista

lista=[]

lista=cargarLista(lista)

print("la lista es: ", lista)