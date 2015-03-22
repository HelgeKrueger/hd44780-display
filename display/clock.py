import datetime
import time

from display import Display

dis = Display()

while True:
    now = datetime.datetime.now()
    print "updating time"
    dis.display_string(now.strftime("%d.%m.%Y %H:%M"), now.strftime("%H:%M:%S"))
    time.sleep(3)
