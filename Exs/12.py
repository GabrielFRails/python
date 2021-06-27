def main():
    valor = float(input('Qual o preço do produto? R$ '))
    valor_disconto = valor - (valor*0.05)
    print(f'O produto com valor {valor} com disconto de 5% passará a custar R$ {valor_disconto :.2f}')

if __name__ == '__main__':
    main()