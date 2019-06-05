#https://pymotw.com/3/threading/


import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
                    )
global zmienna
zmienna = 2000000

def worker():
    global zmienna
    logging.debug('Starting')
    #time.sleep(2)
    zmienna -= 2000000
    logging.debug('Exiting')


def my_service():
    global zmienna
    logging.debug('Starting')
    #time.sleep(3)
    zmienna -= 1000000
    logging.debug('Exiting')


t = threading.Thread(name='my_service', target=my_service)
w = threading.Thread(name='worker', target=worker)
#w2 = threading.Thread(target=worker)  # use default name

w.start()
#w2.start()
t.start()

time.sleep(2)
print(zmienna)
