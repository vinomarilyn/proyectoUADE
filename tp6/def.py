##metodo de burbujeo para ordenar un vector
 arr = [5,2,1,55,84,13,20,11,10]
 band = false
 while band == false:
     band= true
 #iterar con un for
     for i in range(len(arr)-1):
         if arr[i] > arr[i+ 1]:
              aux= arr[i]
              arr[i]= arr[i+1]
              arr[i +1]=aux
              band = false
              
print(arr)
 
        
     


