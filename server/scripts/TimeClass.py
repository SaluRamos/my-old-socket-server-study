import time

class TimeClass:

    def WhatTimeIsIt (time_depht = 5, t_char = "-", end_char = True, letters = False):
        system_time = ""
        ll = ["", "", "", "", ""]
        if(letters == True):
            ll = ["y", "d", "h", "m", "s"]
        #retorna ano
        if(time_depht == 1):
            system_time = time.strftime("%y{0}".format(ll[0]))
        #retorna ano e dia
        elif(time_depht == 2):
            system_time = time.strftime("%y{0}%j{1}".format(ll[0] + t_char, ll[1]))
        #retorna ano, dia e hora
        elif(time_depht == 3):
            system_time = time.strftime("%y{0}%j{1}%H{2}".format(ll[0] + t_char, ll[1] + t_char, ll[2]))
        #retorna ano, dia, hora e minuto
        elif(time_depht == 4):
            system_time = time.strftime("%y{0}%j{1}%H{2}%M{3}".format(ll[0] + t_char, ll[1] + t_char, ll[2] + t_char, ll[3]))
        #retorna ano, dia, hora, minuto e segundo
        elif(time_depht == 5):
            system_time = time.strftime("%y{0}%j{1}%H{2}%M{3}%S{4}".format(ll[0] + t_char, ll[1] + t_char, ll[2] + t_char, ll[3] + t_char, ll[4]))
        #retorna hora, minuto e segundo
        elif(time_depht == 6):
            system_time = time.strftime("%H{0}%M{1}%S{2}".format(ll[2] + t_char, ll[3] + t_char, ll[4]))
        #retorna erro
        else:
            return None
        if(end_char == True):
            system_time = system_time + t_char
        return system_time
