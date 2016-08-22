from microbit import Image, display, sleep, button_a, button_b

image = Image('00100:'
              '00500:'
              '15951:'
              '00500:'
              '00100:')
              
display.show(image)
    
while True:
    if button_a.is_pressed():
        image = image.shift_left(1)
    if button_b.is_pressed():
        image = image.shift_right(1)
    display.show(image)
    sleep(200)