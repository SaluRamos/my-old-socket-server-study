import os
import sys

class FileManipulator:

    #retorna o conteúdo de uma linha (recebe: index)
    #-1 = conteúdo não encontrado
    def ReadIndex (file_name, file_extension, line_index):
        the_file = open(r"" + file_name + file_extension, "r")
        for i, line in enumerate(the_file):
            if i == (line_index - 1):
                return line
        the_file.close()
        return -1

    #retorna o primeiro index de uma linha que contém o conteúdo (recebe: content)
    #-1 = conteúdo não encontrado
    def ReadContent (file_name, file_extension, line_content):
        try:
            the_file = open(r"" + file_name + file_extension, "r")
            lines = the_file.readlines()
            line_index = lines.index(line_content)
            line_index += 1
            the_file.close()
            return line_index
        except:
            return -1

    #retorna primeiro index encontrado de uma linha que possui breaks e um content sendo um desses breaks (recebe: content)
    #-1 = conteúdo não encontrado
    def ReadContentWithBreaking (file_name, file_extension, the_content, breaker = ";"):
        the_file = open(r"" + file_name + file_extension, "r")
        lines = the_file.readlines()
        for i in range(0, len(lines), 1):
            new_line = lines[i].split(breaker)
            for w in range(0, len(new_line), 1):
                if(new_line[w] == the_content):
                    return i + 1
        return -1
        
    #adiciona o conteúdo ao final de um arquivo (recebe: content)
    #não há como falhar
    def AppendEOF (file_name, file_extension, line_content):
        the_file = open(r"" + file_name + file_extension, "a")
        the_file.write("\n" + line_content)
        the_file.close()
        return "conteudo adicionado ao final do arquivo"

    #adiciona o conteúdo ao index de um arquivo (recebe: index e content)
    def AppendIndex (file_name, file_extension, line_index, line_content):
        the_file_one = open(r"" + file_name + file_extension, "r")
        lines = the_file_one.readlines()
        the_file_one.close()
        if(len(lines) < line_index or line_index <= 0):
            return "index não existe"
        the_file_two = open(r"" + file_name + file_extension, "w")
        for i, line in enumerate(lines):
            if(i == (line_index - 1)):
                the_file_two.write(line_content + "\n")
            the_file_two.write(line)
            i += 1
        the_file_two.close()
        return "conteudo adicionado no index"

    #apaga o conteúdo de uma linha (recebe: content)
    #0 = index apagado
    #-1 = conteúdo não encontrado
    def DeleteContent (file_name, file_extension, line_content):
        the_file_one = open(r"" + file_name + file_extension, "r")
        lines = the_file_one.readlines()
        the_file_one.close()
        try:
            try:
                lines.index(line_content + "\n")
            except:
                lines.index(line_content)
            the_file_two = open(r"" + file_name + file_extension, "w")
            for i, line in enumerate(lines):
                if(line.strip("\n") != line_content):
                    if(i == 0):
                        the_file_two.write(line.strip("\n"))
                        the_file_two.write("\n")
                    elif(i == 1):
                        the_file_two.write(line.strip("\n"))
                    else:
                        the_file_two.write("\n" + line.strip("\n"))
            the_file_two.close()
            return 0
        except:
            return -1

    #apaga o conteúdo de uma linha (recebe: index)
    #caso o index não exista, não faz nada
    def DeleteIndex (file_name, file_extension, line_index):
        the_file_one = open(r"" + file_name + file_extension, "r")
        lines = the_file_one.readlines()
        print(sys.getsizeof(lines))
        the_file_one.close()
        if(len(lines) < line_index or line_index <= 0):
            return "index não existe"
        the_file_two = open(r"" + file_name + file_extension, "w")
        w = False
        for i, line in enumerate(lines):
            if(i != (line_index - 1)):
                if(i > 0):
                    if(w == True):
                        w = False
                        the_file_two.write(line.strip("\n"))
                    else:
                        the_file_two.write("\n")
                        the_file_two.write(line.strip("\n"))
                elif(i == 0):
                    the_file_two.write(line.strip("\n"))
            elif(i == 0):
                w = True
        the_file_two.close()
