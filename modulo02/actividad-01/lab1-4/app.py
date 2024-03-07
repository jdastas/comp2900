# Python program to get average of a list 
def Average(lst): 
    return sum(lst) / len(lst) 
 
def promedio(lista_numeros):
    suma = 0  
    ctr = 0  
    for valor in lista_numeros:
        suma = suma + valor #   suma += valor
        ctr = ctr + 1       #   ctr++
    return (suma / ctr)

# Version ChatGPT
lst = [15, 9, 55, 41, 35, 20, 62, 49] 
average = Average(lst) 
print(lst)
print(f'El promedio de la lista es {average}')

# Versioin del Curso
print(lst)
print(f'El valor promedio de la lista es {promedio(lst)}')