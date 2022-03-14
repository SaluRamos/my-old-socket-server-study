#other libs
from tkinter import *

class Variables:

    config_lines = open(r"archives/config.txt", "r").readlines()
    root = Tk()
    menu = Menu(root)
    canvas = Canvas(root, width = 750, height = 545)
    server_dns = config_lines[2].split(";")[1]
    game_version = "ALFA 0.5"
    server_running = False
    stop_server = False
    restart_server = False
    free_server_threads = 0
    whatsapp_driver_queue = []