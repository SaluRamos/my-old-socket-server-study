import threading
import time
import math

#Exemplo de uso do Timer
#timer = Timer(bool_high_precision = True, precision = 0.01, max_time = 5, timer_name = "ReadIndex")
#timer.start()
#timer.ReturnCounter(print_or_not = True, return_or_not = False)
class Timer(threading.Thread):

    finish_timer = False
    counter = 0.0
    precision = 0.0
    high_precision = True
    max_thread_timer = 0.0
    thread_name = ""

    def __init__(self, timer_name, bool_high_precision = True, precision = 0.01, max_time = 10):
        Timer.precision = precision
        Timer.high_precision = bool_high_precision
        Timer.max_thread_timer = max_time
        Timer.thread_name = timer_name
        threading.Thread.__init__(self)
        self.event = threading.Event()
        
    def run(self):
        while (Timer.finish_timer == False):
            time.sleep(Timer.precision)
            if(Timer.high_precision == True):
                Timer.counter += Timer.precision * math.sqrt(math.e)
            else:
                Timer.counter += Timer.precision
            if(Timer.counter >= Timer.max_thread_timer):
                Timer.ReturnCounter(self, False)
                break
    
    def ReturnCounter(self, print_or_not = False, return_or_not = True):
        Timer.finish_timer = True
        time.sleep(0.1)
        if(print_or_not == True):
            print("TIMER " + Timer.thread_name + " = " + "{:.5f} segundos".format(Timer.counter))
        if(return_or_not == True):
            return "{:.5f}" .format(Timer.counter)