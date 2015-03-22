import time

from gpio_wrapper import GpioWrapper

class HD44780Display():
    E_PULSE = 0.00005
    E_DELAY = 0.00005

    def __init__(self, config):
        self.config = config
        self.gpio_wrapper = GpioWrapper(self.config)
        self.data_pins = {0: 'DATA4', 1: 'DATA5', 2: 'DATA6', 3: 'DATA7'}
        self._switch_to_4bit_mode()
        self._cursor_to_start_of_cgram()
        self._display_on()
        self._cursor_move_no_display_shift()
        self.clear_display()

    def _switch_to_4bit_mode(self):
        self._send_command(0x33)
        self._send_command(0x32)

    def _cursor_to_start_of_cgram(self):
        self._send_command(0x28)
    def _display_on(self):
        self._send_command(0x0c)
    def _cursor_move_no_display_shift(self):
        self._send_command(0x06)
    
    def clear_display(self):
        self._send_command(0x01)

    def go_to_line_1(self):
        self._send_command(0x80)
    def go_to_line_2(self):
        self._send_command(0xC0)

    def _send_command(self, byte):
        self.gpio_wrapper.sendOutput('RS', False)
        self._send_byte_to_data_pins(byte)

    def write_byte(self, byte):
        self.gpio_wrapper.sendOutput('RS', True)
        self._send_byte_to_data_pins(byte)

    def _send_byte_to_data_pins(self, byte):
        for block in [4, 0]:
            for index in range(0, 4):
                self.gpio_wrapper.sendOutput(self.data_pins[index], self._is_bit_set(byte, 2 ** (block + index)))
            self._send_pulse()

    def _is_bit_set(self, byte, bit):
        return byte & bit == bit

    def _send_pulse(self):
        time.sleep(self.E_DELAY)    
        self.gpio_wrapper.sendOutput('E', True)
        time.sleep(self.E_PULSE)
        self.gpio_wrapper.sendOutput('E', False)
        time.sleep(self.E_DELAY)      
