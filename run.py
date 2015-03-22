#!/usr/bin/python

import datetime
import sys
import time
import yaml

from display.daemon import Daemon
from display.display import Display
from display.message import Message


class DisplayDaemon(Daemon):
    def run(self):
        config = yaml.load(file('/home/pi/lcd_display/config.yaml', 'r'))
        dis = Display(config['display'])
        msg = Message(config['messages'])

        while True:
            print('test')
            now = datetime.datetime.now()
            time_string = now.strftime("%d.%m.%y %H:%M")
            message = msg.get_message()
            dis.display_string(time_string, message)
            time.sleep(int(config['waittime']))

if __name__ == '__main__':
    daemon = DisplayDaemon('/tmp/lcd_display.pid', stdout = '/tmp/out', stderr = '/tmp/err')
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            daemon.start()
        elif 'stop' == sys.argv[1]:
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        else:
            print("Unknown command")
            sys.exit(2)
        sys.exit(0)
    else:
        print "usage: %s start|stop|restart" % sys.argv[0]
        sys.exit(2)

