'''
BUBBLE SORT
'''

def bubble_sort_paralelo(lista1,lista2):
  for i in range(0, len(lista1)-1):
    for j in range(i+1, len(lista1)):
      if (lista1[j] < lista1[i]):
        aux = lista1[j]
        lista1[j] = lista1[i]
        lista1[i] = aux
        
        aux2 = lista2[j]
        lista2[j] = lista2[i]
        lista2[i] = aux2
        
        
        
  return lista


def bubble_sort(lista):
  for i in range(0, len(lista)-1):
    for j in range(i+1, len(lista)):
      if (lista[j] < lista[i]):
        aux = lista[j]
        lista[j] = lista[i]
        lista[i] = aux
  return lista

numeros = [1,3,4,-5,10,-2,5]
numeros_ordenados = bubble_sort(numeros)
print(f'Lista ordenada por bubble sort: {numeros_ordenados}')

'''
SELECTION SORT
'''
def selection_sort(lista):
  for i in range(0, len(lista)-1):
    pos_minimo = i
    for j in range(i+1, len(lista)):
      if (lista[j] < lista[pos_minimo]):
        pos_minimo = j
    if (pos_minimo != i):
      aux = lista[pos_minimo]
      lista[pos_minimo] = lista[i]
      lista[i] = aux
  return lista

numeros = [1,3,4,-5,10,-2,5]
numeros_ordenados = selection_sort(numeros)
print(f'Lista ordenada por selection sort: {numeros_ordenados}')

'''
INSERTION SORT
'''

def insertion_sort(lista):
  for j in range(1, len(lista)):
    i = j - 1
    pos_actual = j #La variable pos_actual la usamos para cuando tenemos mas de 1 swap por iteracion
    while (i >= 0):
      if (lista[i] > lista[pos_actual]):
        aux = lista[pos_actual]
        lista[pos_actual] = lista[i]
        lista[i] = aux
        pos_actual = i
      i = i - 1
  return lista

numeros = [1,3,4,-5,10,-2,5]
numeros_ordenados = insertion_sort(numeros)
print(f'Lista ordenada por insertion sort: {numeros_ordenados}')