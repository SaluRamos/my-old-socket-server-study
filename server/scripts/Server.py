#other libs
import socket
import threading
#my libs
from scripts.Variables import *
from scripts.Logs import *
from scripts.Solver import *

class Server:

    def StartServer ():
        if(Variables.server_running == True):
            return
        Variables.server_running = True
        Variables.free_server_threads = int(Variables.config_lines[3].split(";")[1])
        try:
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_socket.bind((Variables.config_lines[0].split(";")[1], int(Variables.config_lines[1].split(";")[1])))
            server_socket.listen(10)
        except:
            return
        Variables.menu.server_free_threads.config(bg = "forest green")
        Variables.canvas.itemconfig(Variables.menu.server_status, fill = "forest green")
        Logs.CommandLogTime()
        Logs.CommandLog(" SERVIDOR ONLINE", "start_server_tag", "forest green", backspace = False)
        while(True):
            client_socket, client_address = server_socket.accept()
            if(Variables.restart_server == True):
                Variables.restart_server = False
                Variables.server_running = False
                Variables.menu.server_free_threads.config(bg = "royalblue")
                Variables.canvas.itemconfig(Variables.menu.server_status, fill = "royalblue")
                Logs.CommandLogTime()
                Logs.CommandLog(" REINICIANDO SERVIDOR", "restart_server_tag", "royalblue", backspace = False)
                Variables.free_server_threads = 0
                return
            elif(Variables.stop_server == True):
                Variables.stop_server = False
                Variables.server_running = False
                Variables.menu.server_free_threads.config(bg = "red")
                Variables.canvas.itemconfig(Variables.menu.server_status, fill = "red")
                Logs.CommandLogTime()
                Logs.CommandLog(" SERVIDOR OFFLINE", "closed_server_tag", "red", backspace = False)
                Variables.free_server_threads = 0
                return
            elif(Variables.free_server_threads > 0):
                Variables.free_server_threads -= 1
                threading.Thread(target = Solver.NewSolver, args = (client_socket, client_address), daemon = True).start()

    def StopServer ():
        if(Variables.server_running == True):
            Variables.stop_server = True
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect(("ar2brasil-core.ddns.net", int(Variables.config_lines[1].split(";")[1])))

    def RestartServer ():
        if(Variables.server_running == True):
            Variables.restart_server = True
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect(("ar2brasil-core.ddns.net", int(Variables.config_lines[1].split(";")[1])))
            time.sleep(3)
            Server.StartServer()