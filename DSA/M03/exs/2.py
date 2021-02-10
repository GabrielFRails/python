lista_mercado = ['Abacaxi', 'Leite', 'Creme de Leite', 'ovos', 'Banana']
tam_mercado = len(lista_mercado)
count = 0
for i in range(0, tam_mercado):
    if(lista_mercado[i] == 'Morango'):
        count = 1

if count == 1:
    print('Opa temos morango na lista')
else:
    print('Você esqueceu de adicionar Morango')