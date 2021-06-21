import math

def main():
    n = int(input('Digite um número: '))
    print(f'O dobro de {n} é {n*2}')
    print(f'Seu triplo é {n*3}')
    print(f'Por último, a raiz quadrada de {n} é {math.sqrt(n)}.')
    #também poderia representar a raíz dessa forma -> {n ** (1/2)}, dessa forma não precisando
    #importar o módulo math

if __name__ == '__main__':
    main()