import math

def main():
    listaB = [32,53,85,10,15,17,19]
    soma = 0
    for i in listaB:
        double_i = i * 2
        soma += double_i

    print(soma)

def primeira_func():
    print('Hello World!')

def print_nome(nome):
    print('Hello %s!' %nome)

def soma_num(n1, n2):
    print('numero 1: %d e numero 2: %d' %(n1, n2))
    soma = n1 + n2
    print('a soma dos dois é: %d' %soma)

def numPrimo(num):
    '''
    verificando se um número é primo
    '''
    if(num % 2 == 0 and num > 2):
        return print("Esse número não é primo")
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if(num % i == 0):
            return print("Esse número não é primo")
    return print("Esse número é primo")

def split_text(text):
    return print(text.split(" "))

potencia = lambda x: x**2
par = lambda x: x%2 == 0
string_reversa = lambda str: str[::-1] 
add_number = lambda x,y: x+y

if __name__ == '__main__':
    main()