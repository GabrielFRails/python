def main():
    number = int(input('Digite um número para ver sua tabuada: '))
    print('_' * 12)
    for i in range(1,11):
        print(f'{number} x {i} = {number*i}.')
    print('\nFim da tabuada')
    print('_' * 12)

if __name__ == '__main__':
    main()