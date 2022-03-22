#other libs
import time
import socket
#my libs
from scripts.Variables import Variables
from scripts.Logs import Logs
from scripts.FileManipulator import FileManipulator

class Solver:

    def NewSolver (client_socket, client_address):
        Logs.RequestLogTime()
        Logs.RequestLog(" " + client_address[0] + ":" + str(client_address[1]), "ip_mac", "maroon1", backspace = False)
        try:
            data = client_socket.recv(1024)
            data = str(data)
            data = data[2:len(data) - 1]
            Logs.RequestLog(data)
            try:
                client_socket.send(bytes("OBRIGADO, VAMOS PROCESSAR SEU REQUEST!", encoding = 'utf8'))
            except:
                pass
        except:
            pass
        time.sleep(1)
        Variables.free_server_threads += 1

    def NewCommand (msg, acc, psw):
        total_log_lines = Variables.menu.server_commands_log.get("1.0", END).split("\n")
        if(Variables.server_running == False):
            Logs.CommandLog("NÃO É POSSÍVEL, SERVIDOR ESTÁ FECHADO", "closed_server", "red")
            return
        Logs.CommandLogTime()
        Logs.CommandLog(" usuario: " + acc, backspace = False)
        the_index = FileManipulator.ReadContentWithBreaking(file_name = "archives/adms", file_extension = ".txt", the_content = acc)
        if(the_index == -1):
            Logs.CommandLog("USUARIO INEXISTENTE", "inexistent_user", "red")
        else:
            the_list = []
            the_list = FileManipulator.ReadIndex(file_name = "archives/adms", file_extension = ".txt", line_index = the_index).replace("\n", "").split(";")
            if(psw == the_list[1]):
                Logs.CommandLog(msg, "command", "DarkOrchid1")
            else:
                Logs.CommandLog("SENHA INCORRETA", "incorrect_password", "red")
