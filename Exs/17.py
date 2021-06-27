def main():
    cat1 = float(input('Digite o comprimento do cateto oposto: '))
    cat2 = float(input('Digite o comprimento do cateto adjacente: '))
    hip = ((cat1 ** 2) + (cat2 ** 2)) ** 0.5
    print(f'Com catetos {cat1} e {cat2} temos hipotenusa igual a: {hip:.2f}')

if __name__ == '__main__':
    main()