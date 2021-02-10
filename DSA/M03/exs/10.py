frase = "É melhor, muito melhor, contentar-se com a realidade; se ela não é tão brilhante como os sonhos, tem pelo menos a vantagem de existir."
contador = 0
for i in frase:
    if(i == 'r'):
        contador += 1

print('A letra r aparece %d vezes na frase' %contador)