import time

from gpio_wrapper import GpioWrapper
from hd44780_display import HD44780Display

class Display():
    DISPLAY_WIDTH = 16

    def __init__(self, config):
        self.config = config
        self.hd44780 = HD44780Display(self.config)

    def display_string(self, line1, line2):
        self.hd44780.go_to_line_1()
        self._write_string(line1)
        self.hd44780.go_to_line_2()
        self._write_string(line2)

    def _write_string(self, message):
        message = message.ljust(self.DISPLAY_WIDTH, ' ')  
        for i in range(self.DISPLAY_WIDTH):
            self.hd44780.write_byte(ord(message[i]))
