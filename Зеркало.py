def mirror(arr):
    arr1=arr[:] # мы создаём копию списка
    arr1.reverse()# переварачиваем её
    arr= arr+arr1 # и склеиваем 2 списка
    print(arr)
mirror(['car', 'bow', 'clam', 'drive', 'false', 'green'])
#def mirror(arr): 
   # mirroredPart = arr.reverse() у реверс нет значения поэтому мы не можем его ни к чему присвоить
    #arr = arr + mirroredPart