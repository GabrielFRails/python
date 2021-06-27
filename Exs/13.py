def main():
    salario = float(input('Qual é o atual salário? R$ '))
    aumento = float(input('O aumento será de quantos %? '))
    print(f'Um funcionário que recebe R$ {salario:.2f} receberá um aumento de {aumento}%')
    print(f'Seu novo salário será: R$ {salario * ((aumento + 100) / 100) :.2f}')

if __name__ == '__main__':
    main()