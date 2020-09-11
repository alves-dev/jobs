import schedule
import time
from constants import HORA_IGOR
from work import Igor

def job(m):
    print("Hello World" + m)

def hour():
    print("agora")

#schedule.every(15).seconds.do(job)
schedule.every(1).days.at(HORA_IGOR).do(hour)
i = Igor()
schedule.every(10).seconds.do(i.fudeu, m='igor')

while True:
    schedule.run_pending()
    time.sleep(1)
