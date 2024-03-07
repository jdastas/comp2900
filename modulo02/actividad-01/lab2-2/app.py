def mayor(lista):
    valor_mayor = lista[0]
    for n in lista:
        if (n > valor_mayor):
            valor_mayor = n
    return valor_mayor


lst = [10, 4, 3, 15, 9, 22, 1]
print(lst)
print(f'El valor mayor es {mayor(lst)}')