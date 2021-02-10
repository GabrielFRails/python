"""
x = 0

while(x < 10):
    print('O valor de x nessa iteração é %d' %x)
    print('O valor de X ainda é menor que 10, somando mais um')
    x += 1

else:
    print('cabou o loop, o valor de x é %d' %x)

contador = 0

while(contador < 100):
    if(contador == 5):
        break
    else:
        pass
    print('o valor de couter é %d' %contador)
    contador += 1
"""

for i in range(2,30):
    j = 2
    counter = 0
    while(j<i):
        if(i % j == 0):
            counter = 1
            j += 1
        else:
            j += 1
    if(counter == 0):
        print(str(i) + " é um número primo")
        counter = 0
    else:
        counter = 0