from random import choice
def main():
    n1 = str(input('Digite o nome do primeiro aluno: '))
    n2 = str(input('Digite o nome do segundo aluno: '))
    n3 = str(input('Digite o nome do terceiro aluno: '))
    n4 = str(input('Digite o nome do quarto aluno: '))

    listaAlunos = [n1, n2, n3, n4]
    print(f'O aluno escolhido foi o {choice(listaAlunos)}')

if __name__ == '__main__':
    main()