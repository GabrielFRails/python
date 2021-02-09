"""
nome = input('Digite seu nome: ')
idade = input('Digite a sua idade: ')

if(nome == 'Gabriel' and idade > '17'):
    print('Blz sir Gabriel, pode dirigir')

elif(idade > '17' and nome != 'Gabriel'):
    print('Desconheço vossa senhoria mas tb pode')

else:
    print('no puede dirigir')
"""
disciplina = input('Digite o nome da disciplina: ')
nota_final = input('Digite sua nota final: ')
semestre = input('Digite o semestre que você está(1 a 4): ')

if(disciplina == 'Geografia' and nota_final >= '70' and int(semestre) != 1):
    print('Parabés você foi aprovado em %s com nota final de %r!' %(disciplina, nota_final))
else:
    print('Lamento, estude mais na próxima')