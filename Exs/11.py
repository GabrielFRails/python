def main():
    largura = float(input('Digite a largura da parede: '))
    comprimento = float(input('Digite o comprimento: '))
    area = largura*comprimento;
    print(f'Sua parede tem {largura} x {comprimento} = {area}m².')
    print(f'Será necessário {area*0.5} litros para pintar a parede')

if __name__ == '__main__':
    main()