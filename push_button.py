from gpiozero import LED, Button
from time import sleep

led = LED(14)
button = Button(15)

while True:
    if button.is_pressed:
        led.on()
    else:
        led.off()