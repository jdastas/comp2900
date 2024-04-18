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

for corridas in range(90000, 0, -10000):
    print(f'Organizando {corridas} datos ... Favor esperar')
    lista = []
    f = open("peor_caso.dat", "r")
    for n in f:
        lista.append(n)
    f.close()

    del lista[corridas:] # 10000 elements (debe borrar 90000 elementos)

    tiempo = timeit(bubble_sort(lista))
    print(f'Tiempo: {tiempo} segs')
