import timeit

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

lista = []
f = open("peor_caso.dat", "r")
for n in f:
  lista.append(n)
f.close()

del lista[90000:] # 10000 elements (debe borrar 90000 elementos)

tiempo = timeit(bubble_sort(lista))
print(f'{tiempo} segs')
