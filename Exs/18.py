import math
def main():
    angulo = float(input('Digite um ângulo: '))
    print(f'O ângulo digitado foi {angulo:.2f}.')
    print(f'Seu seno é: {math.sin(math.radians(angulo)):.2f}')
    print(f'Seu cosseno é: {math.cos(math.radians(angulo)):.2f}')
    print(f'Sua tangente tangente é: {math.tan(math.radians(angulo)):.2f}')

if __name__ == '__main__':
    main()