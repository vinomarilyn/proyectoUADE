def cargaLista (lista):
    valor= int(input("Ingrese un valor: "))
    
    while valor != -1:
        lista.append(valor)
        valor= int(input("Ingrese un valor: "))
        
    return lista
    

def mayor(lista):
    max=lista[0]
    for i in range (0, len(lista)):
        if lista[i] > max:
            max = lista[0]
        
    return max
        
def menor(lista):
    menor=lista[0]
    for i in range (0, len(lista)):
        if lista[i] < menor:
            menor = lista[i]
    return menor





#lista= [2, 3, 4, 5, -4]

lista=[]
lista= cargaLista(lista)



mayor=mayor(lista)
menor= menor(lista)
print("El mayor es ", mayor)
print("El menor es ", menor)
print("La lista es: ", lista)
