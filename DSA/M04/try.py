def divisor(num1, num2):
    print(round(num1/num2, 2))

divisor(4,3)
#divisor(4,0)

try:
    8 + 's'
except TypeError:
    print('Operação não permitida')

#vamos abrir um arquivo aqui
try:
    f = open('arquivos/testandoerros.txt','w')
    f.write('Gravando no arquivo')
except IOError:
   print ("Erro: arquivo não encontrado ou não pode ser salvo.")
else:
   print ("Conteúdo gravado com sucesso!")
   f.close()

#agr de propósito vamos simular um erro
try:
    f = open('arquivos/testandoerros','r')
except IOError:
   print ("Erro: arquivo não encontrado ou não pode ser lido.")
else:
   print ("Conteúdo gravado com sucesso!")
   f.close()