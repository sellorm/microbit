# Betty says hello, then winks
from microbit import Image, display, sleep

blink = Image('00000:09000:00000:00000:00000:')

while True:
    display.scroll("Hello, my name is Betty!")
    display.show(Image.HAPPY)
    sleep(500)
    display.show(Image.SMILE + blink)
    sleep(500)
    display.show(Image.HAPPY)
    sleep(2000)
