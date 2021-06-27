def main():
    valor = float(input('Quanto vc tem de money: R$ '))
    print('Considerando U$ 1 = R$ 5.00')
    print(f'Com {valor} você comprar {valor/5} dólares americanos.')

if __name__ == '__main__':
    main()