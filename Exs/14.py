def main():
    temp = float(input('Digite a temperatura em ºC: '))
    tempF = (temp * 9/5) + 32
    print(f'A temperatura {temp} ºC, corresponde a {tempF} ºF')

if __name__ == '__main__':
    main()