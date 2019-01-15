import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

class Led():
    def __init__(self, pinNum):
        GPIO.setup(pinNum, GPIO.OUT)
        self.pinNum = pinNum
        self.state = False
        
    
    def turnOn(self):
        GPIO.output(self.pinNum, GPIO.HIGH)
        self.state = True
        return

    def turnOff(self):
        GPIO.output(self.pinNum, GPIO.LOW)
        self.state = False
        return

    def toggle(self):
        if self.state:
            GPIO.output(self.pinNum, GPIO.LOW)
            self.state = not self.state
        else:
            GPIO.output(self.pinNum, GPIO.HIGH)
            self.state = not self.state
        return
           