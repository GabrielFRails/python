#declarando uma tupla
tupla1 = ("Banana", 23, "macaco")
print(tupla1[0])
print(tupla1[1:])

lista1 = list(tupla1)
print(lista1)

lista1.append('lagartixa')
print(lista1)
lista1 = tuple(lista1)
print(lista1)
