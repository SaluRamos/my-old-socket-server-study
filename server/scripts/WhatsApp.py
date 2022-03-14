#other libs
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import threading
#my libs
from scripts.Variables import *

class WhatsApp:

    the_driver_options = Options()
    the_driver_options.add_argument("user-data-dir=" + r"chrome_driver_data")
    the_driver_options.add_argument("--profile-directory=Profile 1")
    the_driver_options.add_argument("--window-size=800,700")
    the_driver_options.add_argument("--blink-settings=imagesEnabled=false")
    the_driver = webdriver.Chrome(executable_path = r"chromedriver.exe", options = the_driver_options)

    #Variables.whatsapp_driver_queue.append("send_acc_confirmation_token;" + TokenGenerator.GenerateRandomToken(pool_type = TokenGenerator.numbers_token_pool, token_lenght = 8) +";+554396609010;DakovMonster")
    #threading.Thread(target = WhatsApp.SolveQueue, daemon = True).start()
    def SolveQueue ():
        while True:
            if(len(Variables.whatsapp_driver_queue) > 0):
                new_request = Variables.whatsapp_driver_queue[0]
                request_arguments = new_request.split(";")
                if(request_arguments[0] == "send_acc_confirmation_token"):
                    WhatsApp.SendConfirmationToken(the_token = request_arguments[1], target_number = request_arguments[2], target_nickname = request_arguments[3])
                Variables.whatsapp_driver_queue.pop(0)
            else:
                time.sleep(0.5)

    def SendConfirmationToken (the_token, target_number, target_nickname):
        the_link = "https://api.whatsapp.com/send?phone=" + target_number + "&text=Olá *" + target_nickname + "*, aqui esta seu código de segurança para ativar sua conta: *" + the_token + "*"
        WhatsApp.the_driver.get(url = the_link)
        time.sleep(3)
        try:
            login_button = WhatsApp.the_driver.find_element_by_xpath('//*[@id="action-button"]')
            WhatsApp.the_driver.get(url = login_button.get_attribute("href"))
        except:
            pass
        time.sleep(3)
        try:
            send_button = WhatsApp.the_driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]')
            #send_button.click()
        except:
            pass
        time.sleep(3)
    
    #usando essa função não é necessario importar as bibliotecas do selenium para fechar o driver
    def CloseDriver ():
        WhatsApp.the_driver.close()