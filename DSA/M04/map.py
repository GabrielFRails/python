def fahrenheit(T):
    return ((float(9)/5) * T + 32)
def celcius(T):
    return (float(5)/9 * (T-32))

def main():
    temperaturas = [0, 22.5, 40, 100]
    temp_convertida = list(map(fahrenheit, temperaturas))
    print(f'temperaturas convetidas => {temp_convertida}')

    #fazendo com for
    for i in map(celcius, temperaturas):
        print(round(i,2))

    #fazendo com função lambda
    print(list(map(lambda x: round((5.0)/9 * (x-32), 2), temperaturas)))

    #usando a função map para somar duas listas
    a = [1, 3, 5, 7, 9]
    b = [2, 4, 6, 8,10]

    c = list(map(lambda x, y: x+y, a, b))
    print(c)

if __name__ == '__main__':
    main()