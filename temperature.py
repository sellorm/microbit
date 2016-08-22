from microbit import display, temperature, sleep, button_a, button_b

while True:
    tempdeg = "".join((str(temperature()), "c"))
    display.scroll(tempdeg)
    sleep(1000)
    if button_a.was_pressed():
        display.show("A")
        sleep(300)
    elif button_b.was_pressed():
        display.show("B")
        sleep(300)
