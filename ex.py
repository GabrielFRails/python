def main():
    print('Esse programa pega vários valores e ordena em uma lista')
    number = int(input('Quantos números terá a lista: '))
    lista = list()

    for i in range(0, number):
        n = int(input('Digite um valor: '))
        if(i == 0 or n > lista[-1]):
            lista.append(n)
            print(f'Elemento {n} adicionado ao fim da lista')
        else:
            pos = 0
            while pos < len(lista):
                if n <= lista[pos]:
                    lista.insert(pos, n)
                    print(f'Elemento {n} adicionado na posição {pos} da lista')
                    break
                pos += 1
    print(f'Eis a lista ordenada: {lista}')

if __name__ == '__main__':
    main()
