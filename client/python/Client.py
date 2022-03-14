import socket
import os
import sys

class Core ():

    server_ip = ""
    server_port = 0

    standart_ip = "ar2brasilcore.ddns.net"
    standart_port = 15565

    def Main (arg_one):
        message = ""
        if(arg_one == 1):
            #definindo o ip
            Core.server_ip = Core.standart_ip
            Core.server_ip = socket.gethostbyname(Core.server_ip)
            #definindo a porta
            Core.server_port = Core.standart_port
            #definindo a mensagem
            message = "Hello, World!"
            Core.DoRequest(message)
        else:
            #definindo o ip
            Core.server_ip = input("DIGITE IP PARA CONECTAR: ")
            if(Core.server_ip == ""):
                Core.server_ip = Core.standart_ip
            Core.server_ip = socket.gethostbyname(Core.server_ip)
            #definindo a porta
            server_port_buffer = input("DIGITE A PORTA PARA CONECTAR: ")
            if(server_port_buffer == ""):
                Core.server_port = Core.standart_port
            else:
                Core.server_port = int(server_port_buffer)
            #definindo a mensagem
            message = input("DIGITE MENSAGEM: ")
            if(message == ""):
                message = "Hello, World!"
            #fazer request
            Core.DoRequest(message)

    def DoRequest (message):
        print("\nTENTANDO CONEXÃO COM: " + Core.server_ip + ":" + repr(Core.server_port))
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.connect((Core.server_ip, Core.server_port))
        print("CONEXÃO ESTABELECIDA!\n")
        server_socket.send(bytes(message, encoding='utf8'))
        Core.WaitResponse(server_socket)

    def WaitResponse (server_socket):
        global arg_one
        data = repr(server_socket.recv(1024))
        data = data[2:len(data) - 1]
        print("MENSAGEM RECEBIDA = " + data)
        server_socket.close()
        if(arg_one == 1):
            os._exit(0)
        else:
            input()

os.system("cls")
try:
    arg_one = int(sys.argv[1])
except:
    arg_one = 0
Core.Main(arg_one)