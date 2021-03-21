from functools import reduce

if __name__ == '__main__':

    lista = [47, 11, 42, 13]
    print(f'printando a lista {lista}')

    #criando uma lambda para somar dois valores
    soma = lambda x, y: x+y
    print(f'soma da lista = {round(float(reduce(soma, lista)), 2)}')

    max_number = lambda x, y: x if (x>y) else y
    print(f'maior número encontrado na lista: {reduce(max_number, lista)}')