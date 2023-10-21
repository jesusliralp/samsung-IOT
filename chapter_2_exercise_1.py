from gpiozero import LED, Button

LED_GREEN_PIN = 14
LED_AMBER_PIN = 15
LED_RED_PIN = 16
PUSH_BUTTON_PIN = 17

LED_GREEN = LED(LED_GREEN_PIN)
LED_AMBER = LED(LED_AMBER_PIN)
LED_RED = LED(LED_RED_PIN)
PUSH_BUTTON = LED(PUSH_BUTTON_PIN)

LEDS = [LED_GREEN, LED_AMBER, LED_RED]

SELECTED_LED_IDX = 0

def onButtonPressed():
    SELECTED_LED_IDX = (SELECTED_LED_IDX + 1) % len(LEDS)
    turnOnSelectedLed()

def turnOnSelectedLed():
    for led in LEDS:
        led.off()

    led = LEDS[SELECTED_LED_IDX]
    led.on()

turnOnSelectedLed()

PUSH_BUTTON.when_pressed = onButtonPressed