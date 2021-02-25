def main():
    print('Bem vindo a calculadora em Python ser humaninho!')
    print('Selecione uma opção:\n\n1-Adição\n2-Subtração\n3-Multiplicação\n4-Divisão\n')
    option = int(input('Digite sua escolha: '))
    
    if option == 1:
        n1, n2 = input('Digite dois números: ').split(" ")
        n1 = int(n1)
        n2 = int(n2)
        adiçao(n1, n2)
    elif option == 2:
        n1, n2 = input('Digite dois números: ').split(" ")
        n1 = int(n1)
        n2 = int(n2)
        subtraçao(n1, n2)
    elif option == 3:
        n1, n2 = input('Digite dois números: ').split(" ")
        n1 = int(n1)
        n2 = int(n2)
        multiplicaçao(n1, n2)
    elif option == 4:
        n1, n2 = input('Digite dois números: ').split(" ")
        n1 = int(n1)
        n2 = int(n2)
        divisao(n1, n2)
    else:
        print('Opção inválida, programa encerrado')

def adiçao(n1, n2):
    print(f'{n1} + {n2} = {n1+n2}')

def subtraçao(n1, n2):
    print(f'{n1} - {n2} = {n1-n2}')

def multiplicaçao(n1,n2):
    print(f'{n1} x {n2} = {n1*n2}')

def divisao(n1, n2):
    print(f'{n1} / {n2} = {n1/n2}')

if __name__ == '__main__':
    main()