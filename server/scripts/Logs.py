#my libs
from scripts.Variables import *
from scripts.TimeClass import *
from scripts.FileManipulator import *

class Logs:

    def CommandLog (msg, tagname = "some", tagcolor = "white", backspace = True):
        if(Variables.menu.server_commands_log.get("1.0", END) != "\n" and backspace == True):
            Variables.menu.server_commands_log.insert(END, "\n")
        total_log_lines = Variables.menu.server_commands_log.get("1.0", END).split("\n")
        total_log_lines = total_log_lines[:-1]
        first_logline_char_index = len(total_log_lines[len(total_log_lines) - 1])
        Variables.menu.server_commands_log.insert(END, msg)
        if(tagname != "some"):
            total_log_lines = Variables.menu.server_commands_log.get("1.0", END).split("\n")
            total_log_lines = total_log_lines[:-1]
            last_logline_char_index = len(total_log_lines[len(total_log_lines) - 1])
            Variables.menu.server_commands_log.tag_add(tagname, str(len(total_log_lines)) + "." + str(first_logline_char_index), str(len(total_log_lines)) + "." + str(last_logline_char_index))
            Variables.menu.server_commands_log.tag_configure(tagname, foreground = tagcolor)
        Variables.menu.server_commands_log.see(END)

    #só se usa backspace False aqui em casos muito especificos de primeira linha do log!
    def CommandLogTime (backspace = True):
        if(Variables.menu.server_commands_log.get("1.0", END) == "\n"):
            backspace = False
        if(backspace == True):
            Variables.menu.server_commands_log.insert(END, "\n")
        total_log_lines = Variables.menu.server_commands_log.get("1.0", END).split("\n")
        total_log_lines = total_log_lines[:-1]
        first_logline_char_index = len(total_log_lines[len(total_log_lines) - 1])
        Variables.menu.server_commands_log.insert(END, TimeClass.WhatTimeIsIt(time_depht = 6, end_char = False, letters = True))
        Variables.menu.server_commands_log.tag_add("time", str(len(total_log_lines)) + "." + str(first_logline_char_index), str(len(total_log_lines)) + "." + str(first_logline_char_index + 11))
        Variables.menu.server_commands_log.tag_configure("time", foreground = "tan1")
        Variables.menu.server_commands_log.see(END)

    def RequestLog (msg, tagname = "some", tagcolor = "white", backspace = True):
        if(Variables.menu.server_requests_log.get("1.0", END) != "\n" and backspace == True):
            Variables.menu.server_requests_log.insert(END, "\n")
        total_log_lines = Variables.menu.server_requests_log.get("1.0", END).split("\n")
        total_log_lines = total_log_lines[:-1]
        first_logline_char_index = len(total_log_lines[len(total_log_lines) - 1])
        Variables.menu.server_requests_log.insert(END, msg)
        if(tagname != "some"):
            total_log_lines = Variables.menu.server_requests_log.get("1.0", END).split("\n")
            total_log_lines = total_log_lines[:-1]
            last_logline_char_index = len(total_log_lines[len(total_log_lines) - 1])
            Variables.menu.server_requests_log.tag_add(tagname, str(len(total_log_lines)) + "." + str(first_logline_char_index), str(len(total_log_lines)) + "." + str(last_logline_char_index))
            Variables.menu.server_requests_log.tag_configure(tagname, foreground = tagcolor)
        Variables.menu.server_requests_log.see(END)

    def RequestLogTime (backspace = True):
        if(Variables.menu.server_requests_log.get("1.0", END) == "\n"):
            backspace = False
        if(backspace == True):
            Variables.menu.server_requests_log.insert(END, "\n")
        total_log_lines = Variables.menu.server_requests_log.get("1.0", END).split("\n")
        total_log_lines = total_log_lines[:-1]
        first_logline_char_index = len(total_log_lines[len(total_log_lines) - 1])
        Variables.menu.server_requests_log.insert(END, TimeClass.WhatTimeIsIt(time_depht = 6, end_char = False, letters = True))
        Variables.menu.server_requests_log.tag_add("time", str(len(total_log_lines)) + "." + str(first_logline_char_index), str(len(total_log_lines)) + "." + str(first_logline_char_index + 11))
        Variables.menu.server_requests_log.tag_configure("time", foreground = "tan1")
        Variables.menu.server_requests_log.see(END)