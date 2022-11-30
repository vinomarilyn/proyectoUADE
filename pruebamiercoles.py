def comparador(n)
v=[]
acu = 0
for i in range(0,5):
    n= int(input("ingrese un numero: "))
    v.append(n)
    acu = acu + v[i]

promedio=acu/5
  # lista=v
    
print("lista: ", v)
print("promedio ", promedio)
    
