'''
BUSQUEDA SECUENCIAL BASICA
Si no está el elemento en la lista devuelve -1
'''

def busqueda_secuencial_basica(lista, valor_buscado):
  posicion = -1
  for i in range(len(lista)):
    if (lista[i] == valor_buscado):
      posicion = i
  return posicion
    

'''
BUSQUEDA SECUENCIAL MEJORADA
Si no está el elemento en la lista devuelve -1
'''
def busqueda_secuencial(lista, valor_buscado):
  posicion = -1
  i = 0
  while (posicion == -1 and i < len(lista)):
    if (lista[i] == valor_buscado):
      posicion = i
    i = i + 1
  return posicion

def informarMismoPrecio(lista1,lista2, valor_buscado):
  
  print("INFORMAMOS CODIGOS DE PRODUCTOS CON PRECIO $" + str(valor_buscado))
  for i in range(len(lista1)):
    if (lista1[i] == valor_buscado):
      print(lista2[i])


def funcionEjemplo():
    nuevosPrecios=[500,600,300,400,500]
    return (nuevosPrecios)


'''
BUSQUEDA BINARIA
Precondicion: La lista debe estar previamente ordenada
'''
def busqueda_binaria(lista, valor_buscado):
  posicion = -1
  izq = 0
  der = len(lista)-1
  while (posicion == -1 and izq <= der):
    medio = (izq + der) // 2
    if (lista[medio] == valor_buscado):
      posicion = medio
    else:
      #Mi valor buscado puede estar a la derecha del medio
      if (valor_buscado > lista[medio]):
        izq = medio + 1
      else:
        # Si el valor buscado esta a la izquierda del medio
        der = medio - 1
  return posicion

#En este caso, los apellidos estan ordenados alfabeticamente para poder usar busqueda binaria
apellidos = ['Gomez', 'Perez', 'Quintana']
pos = busqueda_binaria(apellidos, 'Perez')


vCodigo =[1000,2000,3000,4000,5000]
vPrecio=[100,200,300,400,500]
pos = busqueda_secuencial(vCodigo,1000)

if pos >= 0 :
    print("CODIGO VALIDO")
else:
    print("CODIGO INVALIDO")

nuevoPrecio=funcionEjemplo()

print(pos)

