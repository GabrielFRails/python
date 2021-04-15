'''def askint():
    while True:
        try:
            var = int(input('Digite um número: '))
        except:
            print('você não digitou um número')
            continue
        else:
            print('ae finalmente um número')
            break
        finally:
            print('The end!')
        print(var)

askint()'''

tuple = (1,2,3,4,5)
try:
    tuple.append(6)
    for each in tuple:
        print(each)
except AttributeError as e:
    print('Erro: ', e)
except IOError as e:
    print('Erro de I/O:', e)
