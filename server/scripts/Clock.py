#other libs
import time
import threading
#my libs
from scripts.Variables import Variables
from scripts.Logs import Logs
from scripts.TimeClass import TimeClass
from scripts.Server import Server

class Clock:

    def TheClock():
        while(True):
            Variables.config_lines = open(r"archives/config.txt", "r").readlines()
            #auto restart
            if(TimeClass.WhatTimeIsIt(time_depht = 6, end_char = False) == Variables.config_lines[9].split(";")[1] and Variables.server_running == True):
                #salvar logs e resetar os campos
                the_command_log = open(r"logs/commands_logs/" + TimeClass.WhatTimeIsIt(time_depht = 5, end_char = False, letters = True) + " command_log.log", "w")
                the_command_log.write(Variables.menu.server_commands_log.get("1.0", END))
                the_command_log.close()
                Variables.menu.server_commands_log.delete("1.0", END)
                the_requests_log = open(r"logs/requests_logs/" + TimeClass.WhatTimeIsIt(time_depht = 5, end_char = False, letters = True) + " requests_log.log", "w")
                the_requests_log.write(Variables.menu.server_requests_log.get("1.0", END))
                the_requests_log.close()
                Variables.menu.server_requests_log.delete("1.0", END)
                #anunciar reinicio
                Logs.CommandLogTime()
                Logs.CommandLog(" REINICIO AUTOMATICO", "restart_server_tag", "royalblue", backspace = False)
                Logs.CommandLogTime()
                Logs.CommandLog(" SALVANDO LOGS", "saving_logs", "gold", backspace = False)
                threading.Thread(target = Server.RestartServer, daemon = True).start()
            #att free_threads
            Variables.menu.server_free_threads.config(text = str(Variables.free_server_threads))
            #sleep
            time.sleep(1)