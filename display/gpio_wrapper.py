import RPi.GPIO as GPIO

class GpioWrapper():
    def __init__(self, config):
        self.config = config

        GPIO.setmode(GPIO.BCM)

        datapins = ['E', 'RS', 'DATA4', 'DATA5', 'DATA6', 'DATA7']
        for pin in datapins:
            GPIO.setup(int(self.config[pin]), GPIO.OUT)

    def __del__(self):
        GPIO.cleanup()

    def sendOutput(self, pinName, signal):
        GPIO.output(self.config[pinName], signal)
