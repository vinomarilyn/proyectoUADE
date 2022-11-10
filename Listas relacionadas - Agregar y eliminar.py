'''
Cargar los legajos y apellidos de los alumnos de un curso en dos listas relacionadas.

Luego de finalizar la carga, mostrar ambos con el formato:
Legajo: xxx - Apellido: xxx
'''

# 1. Carga de los datos
legajos = []
apellidos = []
cantidad = int(input('Ingrese la cantidad de alumnos: '))
for i in range(0, cantidad):
  legajo = int(input('Ingrese legajo: '))
  apellido = (input('Ingrese apellido: '))
  legajos.append(legajo)
  apellidos.append(apellido)

# 2. Mostrar los resultados
for i in range(0, len(apellidos)): #len(legajos) es lo mismo que len(apellidos) justamente por ser "listas relacionadas"
  print(f'Legajo: {legajos[i]} - Apellido: {apellidos[i]}')

'''
Ahora se le pide al usuario el apellido de un alumno, y si ese alumno pertenece al curso hay que eliminarlo
'''
# 3. Eliminar valores en listas relacionadas
def busqueda_secuencial(lista, valor_buscado):
  posicion = -1
  i = 0
  while (posicion == -1 and i < len(lista)):
    if (lista[i] == valor_buscado):
      posicion = i
    i = i + 1
  return posicion

apellido_buscado = input('Ingrese el apellido a eliminar: ')
posicion = busqueda_secuencial(apellidos, apellido_buscado)
if (posicion == -1):
  print('El apellido no pertenece al curso')
else:
  apellidos.pop(posicion)
  legajos.pop(posicion)

# 4. Muestro como quedaron las listas
for i in range(0, len(apellidos)):
  print(f'Legajo: {legajos[i]} - Apellido: {apellidos[i]}')