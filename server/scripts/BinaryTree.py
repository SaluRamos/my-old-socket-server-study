#other libs

#my libs
from scripts.TimeClass import *

class BinaryTree:

    #salva o idxmap de um arquivo em formato de arquivo
    def CreateIndexMap (the_file_name, the_file_extension):
        the_file_read = open(r"" + the_file_name + the_file_extension, "r")
        file_lines = the_file_read.readlines()
        idxmap = []
        for i in range(0, len(file_lines), 1):
            idxmap.append(len(file_lines[i]))
        the_file_read.close()
        return idxmap

    #retorna o total de bytes até certa linha de um arquivo
    #a soma dos bytes é feita a partir do idxmap
    def LinesBytesSum (index, idxmap):
        total_bytes = 0
        for i in range(0, index - 1, 1):
            total_bytes += int(idxmap[i])
        return total_bytes

    def IndexAdd (the_string, index, idxmap, the_file_name, the_file_extension):
        the_file = open(r"" + the_file_name + the_file_extension, "r+")
        local = BinaryTree.LinesBytesSum(index = index, idxmap = idxmap)
        the_file.seek(local)
        the_file.write(the_string + "\n")
        the_file.close()

    #procura um valor dentro de uma lista organizada em ordem crescente!
    #retorna o index da linha encontrada
    def BinarySearch (idxmap, the_file, the_extension, the_content, breaker = ";"):
        pass

    #procura o local do valor apropriado para adicionar um numero
    def BinaryAdd ():
        pass

cache_idxmap = BinaryTree.CreateIndexMap(the_file_name = "database/teste", the_file_extension = ".db")
#adicionar string a um arquivo db
BinaryTree.IndexAdd(the_string = "\nteste_doido", index = 3, idxmap = cache_idxmap, the_file_name = "database/teste", the_file_extension = ".db")
