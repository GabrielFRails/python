def main():
    #Abrindo o arquivo
    arq1 = open("arquivos/arquivo1.txt", "r")
    #Lendo o conteúdo do arquivo
    print(arq1.read())
    #Contar número de caracteres
    print(arq1.tell())
    #Retornar para o início do arquivo
    print(arq1.seek(0,0))
    #Ler os primeiros 10 caracteres
    print(arq1.read(10))
    arq1.close()

    arq2 = open("arquivos/arquivo1.txt", "a")
    arq2.write("\nBom dia queridos, mexendo com arquivos em python!")
    arq2.close()
    arq2 = open("arquivos/arquivo1.txt", "r")
    print(arq2.read())

if __name__ == '__main__':
    main()