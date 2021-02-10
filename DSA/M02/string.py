#concatenação
nome1, nome2 = "Tim", "Cook"
nome = nome1 + " " + nome2
print('best CEO is %s.' %nome)
print(nome[3])

#slicing com : -> mostra a string a partir daquele ponto
print(nome[4:])
#do contrário só vai até aquele ponto
print(nome[:4])

#também podemos ler de trás para frente
print(nome[-1])
print(nome[:-1])

#podemos fatiar a string em pedaços específicos usando ::
print(nome[::1])
print(nome[::2])

s = 'best apple CEO is '
s = s + nome
print(s)

#algumas funções built-in
print('Botando em maiúsculo %s.' %s.upper())
print('Botando em minúsculo %s.' %s.lower())
print('Cortando as palavras da string %s' %s.split())

#apenas a primeira maiúscula
print(s.capitalize())

#mais funções interessantes
print(s.count('e')) #conta quantas vezes determinado caracter aparece
print(s.find('e')) #mostra a primeira ocorrência de determinado caracter
print(s.islower()) # toda a string é minúscula?
print(s.isspace()) # a string é só espaço?
print(s.endswith('a')) # a string termina com esse caracter?

#comparação de string
print("Python" == "Python")