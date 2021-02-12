def main():
    '''celsius = [39.2, 36.5, 37.3, 37.8]
    fahrenheit = map(lambda x: (float(x * 9/5)) + 32, celsius)
    print(list(fahrenheit))'''
    dic = {'k1': 'Natal', 'k2': 'Recife'}
    print(dir(dic))

def print_sequencia():
    for i in range(0,20):
        print(i+1)

def print_maiusculo(str):
    print(str.upper())

def nova_lista(lista):
    lista.append(5)
    lista.append(6)

def print_num(arg1, *lista):
    print(arg1)
    for i in lista:
        print(i)
    return

if __name__ == '__main__':
    main()