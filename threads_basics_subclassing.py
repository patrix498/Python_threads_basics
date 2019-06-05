import threading
import logging


class MyThread(threading.Thread):

    def run(self):
        logging.debug('running')


logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-8s) %(message)s',
)

for i in range(5):
    t = MyThread()
    t.start()