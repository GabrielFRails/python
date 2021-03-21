seq = ['a', 'b', 'c']
print(list(enumerate(seq)))

for ind, val in enumerate(seq):
    print(ind, val)

for ind, val in enumerate(seq):
    if ind >= 2:
        break
    else:
        print(val)

lista = ['Marketing', 'COmputação', 'Letras']
for i, item in enumerate(lista):
    print(f'curso {i+1}: {item}')

for i, item in enumerate('Isso é uma string meu chapa'):
    print(i, item)

for i, item in enumerate(range(10)):
    print(i, item)