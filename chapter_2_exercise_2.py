from gpiozero import LED
from gpiozero import DistanceSensor
import time

sensor = DistanceSensor(echo = 14, trigger = 15)
amarillo = LED(18)
blau = LED(2)
rot = LED(3)
while True:
    distance = sensor.distance * 1000
    print("distance : ", distance)
    if distance <20:
        amarillo.off()
        blau.off()
        rot.on()
    elif distance <80:
        amarillo.off()
        blau.on()
        rot.off()
    else:
        amarillo.on()
        blau.off()
        rot.off()
    time.sleep(0.5)