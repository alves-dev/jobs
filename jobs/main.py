import schedule
import time
from constants import HORA_IGOR
from work import Igor
import threading

def job(m):
    print("Hello World" + m)

def hour():
    print("agora")

def thad():
    #schedule.every(15).seconds.do(job)
    schedule.every(1).days.at(HORA_IGOR).do(hour)
    i = Igor()
    schedule.every(10).seconds.do(i.fudeu, m='igor')

    while True:
        schedule.run_pending()
        time.sleep(1)


threading.Thread(target=thad).start()
while True:
    print('- ' * 5)
    time.sleep(3)
