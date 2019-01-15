import led
import time

l = led.Led(18)

l.toggle()
time.sleep(1)
l.toggle()