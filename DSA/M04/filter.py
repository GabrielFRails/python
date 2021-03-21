def impar_par(number):
    if number % 2 == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(numbers_list)

    print(f'tipo: {filter(impar_par, numbers_list)}')
    print(f'lista em si: {list(filter(impar_par, numbers_list))}')

    pares = list(filter(lambda x: x%2 == 0, numbers_list))
    impares = list(filter(lambda x: x%2 != 0, numbers_list))

    print(f'Números pares: {pares}, ímpares: {impares}')
    