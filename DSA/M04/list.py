#List Comprehension

if __name__ == '__main__':
    #retornando cada caracter
    lista = [x for x in 'python']
    print(lista)

    #retornando o quadrado de cada numero de uma sequência
    lista_b = [x**2 for x in range(0, 11)]
    print(lista_b)

    #retornando apenas números pares ou ímpares de uma sequência
    lista_pares = [x for x in range(0,21) if x % 2 == 0]
    lista_impares = [x for x in range(0,21) if x % 2 != 0]
    print(f'pares: {lista_pares}\nímpares: {lista_impares}')

    #converter celcius para fahrenheit
    celcius = [0, 10, 20.1, 34.5]
    fahrenheit = [((float(9)/5)*temp + 32) for temp in celcius]
    print(fahrenheit)

    #cada iteração mais profunda eleva ao quadrado o número anterior, nesse caso temos x⁴
    lista_aninhada = [x**2 for x in [x**2 for x in range(11)]]
    print(lista_aninhada)

    # nesse temos x⁸
    lista_aninhada = [x**2 for x in [x**2 for x in [x**2 for x in range(11)]]]
    print(lista_aninhada)