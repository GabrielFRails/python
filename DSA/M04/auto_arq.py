def main():
    file_name = input('Digite o nome do arquivo: ')
    file_name = "arquivos/" + file_name + ".txt"
    arq = open(file_name, "w")
    arq.write('Escrevendo no arquivo')
    arq.close
    arq = open(file_name, "r")
    print(arq.read())
    arq.close

if __name__ == "__main__":
    main()