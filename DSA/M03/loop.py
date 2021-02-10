lista = [1,2,3]
soma = 0

for i in lista:
    double_i = i * 2
    soma += double_i
print(soma)

lista_new = [[2,3,4], [10,20,30], [120, 200, 450]]
for i in lista_new:
    print(i)

dct = {'k1': 'Gabriel', 'k2': 'Pedro', 'k3': 'Lucas'}

for k,v in dct.items():
    print(k,v)

"""
tp = (2,3,4)
lista_marcado = ["Leite", "Ovo", "Banana"]

for i in tp:
    print("Elemento %d" %i)

for i in lista_marcado:
    print(i)

for i in range(0,5):
    print(i)

lista_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in lista_numbers:
    if(i%2 == 0):
        print(i)

for caracter in "Meu nome é Gabriel":
    print(caracter)
"""