def main():
    km = float(input('Digite os km rodados: '))
    dias = int(input('Por quantos dias o carro foi alugado? '))
    precoDias = dias * 60
    precoKm =  km * 0.15
    print(f'O valor final a ser pago é: R$ {(precoDias+precoKm):.2f}')

if __name__ == '__main__':
    main()