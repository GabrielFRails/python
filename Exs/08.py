def main():
    medida = float(input('Digite a distância em metros: '))
    print(f'Dist. em km: {medida/1000}')
    print(f'Dist. em hm: {medida/100}')
    print(f'Dist. em dam: {medida/10}')
    print(f'Dist. em dm: {medida*10}')
    print(f'Dist. em cm: {medida*100}')
    print(f'Dist. em mm: {medida*1000}')

if __name__ == '__main__':
    main()