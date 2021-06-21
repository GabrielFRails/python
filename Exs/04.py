def main():
    a = input('Digite algo: ')
    print(f'O tipo primitivo da variável é: {type(a)}')
    print('Só tem espaços?', a.isspace())
    print('é um número? ', a.isnumeric())
    print('é alfbético? ', a.isalpha())
    print('é alfanumérico?³ ', a.isalnum())
    print('Está em maiscúlo? ', a.isupper())
    print('Está em minúsculo? ', a.islower())
    print('Está Capitalizada? ', a.istitle())

if __name__ == '__main__':
    main()
