#função zip -> unir duas listas em tuplas

def swap_valores(d1, d2):
    dicTemp = {}

    for d1Key, d2Val in zip(d1, d2.values()):
        dicTemp[d1Key] = d2Val

    return dicTemp 

if __name__ == '__main__':

    x = [1, 2, 3]
    y = [4, 5, 6]
    #como retorna um iterator precisamos printar como lista de tuplas
    print(list(zip(x,y)))

    #atenção quando o numero de elementos forem diferentes
    print(list(zip('ABCD', 'xyz')))

    a = [1, 2, 3]
    b = [4, 5, 6, 7, 8]
    print(list(zip(a, b))) 

    #mexendo com dicionários
    d1 = {
        'a': 1,
        'b': 2,
    }   
    d2 = {
        'c': 4,
        'd': 5
    }
    #unindo as chaves
    print(list(zip(d1, d2)))
    #unindo chave de um e valores do outro
    print(list(zip(d1, d2.values())))

    #fazendo com a função
    print(swap_valores(d1, d2))