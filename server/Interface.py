#other libs
import os
import sys
from tkinter import *
import threading
import time
import subprocess
#my libs
from scripts.Variables import Variables
from scripts.Solver import Solver
from scripts.Server import Server
from scripts.Clock import Clock
from scripts.BinaryTree import BinaryTree
from scripts.TokenGenerator import TokenGenerator

class Interface:
    
    def Core ():
        #start button
        Variables.menu.start_server_button = Button(Variables.root, text = "INICIAR", font = ("Arial", "12", "bold"), command = lambda : threading.Thread(target = Server.StartServer, daemon = True).start())
        Variables.menu.start_server_button.place(x = 5, y = 481, width = 115, height = 28)
        #stop button
        Variables.menu.stop_server_button = Button(Variables.root, text = "PARAR", font = ("Arial", "12", "bold"), command = lambda : threading.Thread(target = Server.StopServer, daemon = True).start())
        Variables.menu.stop_server_button.place(x = 130, y = 481, width = 115, height = 29)
        #restart button
        Variables.menu.restart_server_button = Button(Variables.root, text = "REINICIAR", font = ("Arial", "12", "bold"), command = lambda : threading.Thread(target = Server.RestartServer, daemon = True).start())
        Variables.menu.restart_server_button.place(x = 5, y = 513, width = 115, height = 28)
        #server status
        Variables.menu.server_status = Variables.canvas.create_rectangle(130, 513, 244, 540, fill = "red", outline = "")
        #atual free threads
        Variables.menu.server_free_threads = Label(Variables.root, text = str(Variables.free_server_threads), font = ("Arial", "13", "bold"), bg = "red" , fg = "white")
        Variables.menu.server_free_threads.place(x = 180, y = 515)
        #requests label
        Variables.menu.server_requests_label = Label(Variables.root, text = "REQUESTS:", font = ("Arial", "18", "bold"))
        Variables.menu.server_requests_label.place(x = 55, y = 0)
        #requests log
        Variables.menu.server_requests_log = Text(Variables.root, font = ("Arial", "7", "bold"), bg = "black", fg = "white")
        Variables.menu.server_requests_log.place(x = 5, y = 30, width = 240, height = 443)
        #commands label
        Variables.menu.server_commands_label = Label(Variables.root, text = "COMANDOS:", font = ("Arial", "18", "bold"))
        Variables.menu.server_commands_label.place(x = 295, y = 0)
        #commands log
        Variables.menu.server_commands_log = Text(Variables.root, font = ("Arial", "7", "bold"), bg = "black", fg = "white")
        Variables.menu.server_commands_log.place(x = 250, y = 30, width = 240, height = 443)
        #commands user label
        Variables.menu.server_commands_user_label = Label(Variables.root, text = "USUARIO", font = ("Arial", "8", "bold"))
        Variables.menu.server_commands_user_label.place(x = 250, y = 480)
        #commands user entry
        Variables.menu.server_commands_user_entry = Entry(Variables.root, font = ("Arial", "10"), width = 17)
        Variables.menu.server_commands_user_entry.place(x = 310, y = 481, height = 17)
        Variables.menu.server_commands_user_entry.insert(END, Variables.config_lines[4].split(";")[1])
        #commands password label
        Variables.menu.server_commands_password_label = Label(Variables.root, text = "SENHA", font = ("Arial", "8", "bold"))
        Variables.menu.server_commands_password_label.place(x = 250, y = 501)
        #commands password entry
        Variables.menu.server_commands_password_entry = Entry(Variables.root, font = ("Arial", "10"), width = 17, show = "*")
        Variables.menu.server_commands_password_entry.place(x = 310, y = 502, height = 17)
        Variables.menu.server_commands_password_entry.insert(END, Variables.config_lines[5].split(";")[1])
        #commands entry
        Variables.menu.server_commands_entry = Entry(Variables.root, font = ("Arial", "10"), width = 25)
        Variables.menu.server_commands_entry.place(x = 254, y = 522, height = 17)
        Variables.menu.server_commands_entry.insert(END, "INSIRA COMANDO")
        #commands button
        Variables.menu.server_commands_button = Button(Variables.root, text = "ENVIAR\nCOMANDO", font = ("Arial", "7", "bold"), command = lambda : threading.Thread(target = Solver.NewCommand, args = (Variables.menu.server_commands_entry.get(), Variables.menu.server_commands_user_entry.get(), Variables.menu.server_commands_password_entry.get()), daemon = True).start(), width = 7)
        Variables.menu.server_commands_button.place(x = 437, y = 480, height = 60)

    def CascadeFunction (the_file_path):
        os.system("notepad.exe {0}" .format(the_file_path))

os.system("cls")
subprocess.Popen(Variables.config_lines[6].split(";")[1])
Variables.menu.add_cascade(label = "CONFIGURAÇÕES", command = lambda : threading.Thread(target = Interface.CascadeFunction("archives/config.txt"), daemon = True).start())
Variables.menu.add_cascade(label = "ADMINISTRADORES", command = lambda : threading.Thread(target = Interface.CascadeFunction("archives/adms.txt"), daemon = True).start())
Variables.menu.add_cascade(label = "ATUALIZAR TERMOS DE USO", command = lambda : threading.Thread(target = Interface.CascadeFunction("archives/termos.txt"), daemon = True).start())
Variables.root.resizable(False, False)
Variables.root.geometry("495x545")
Variables.root.config(menu = Variables.menu)
Variables.root.iconbitmap(r"archives/icon.ico")
Variables.root.title("ALWAYS RUN SERVER - " + Variables.server_dns + " - " + Variables.game_version)
Variables.canvas.place(x = 0, y = 0)
Interface.Core()
threading.Thread(target = Clock.TheClock, daemon = True).start()
Variables.root.mainloop()