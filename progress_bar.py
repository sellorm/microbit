from microbit import Image, display

image1 = Image('00000:00000:12300:00000:00000:')
image2 = Image('00000:00000:01230:00000:00000:')
image3 = Image('00000:00000:00123:00000:00000:')
image4 = Image('00000:00000:30012:00000:00000:')
image5 = Image('00000:00000:23001:00000:00000:')
image = (image1, image2, image3, image4, image5)

while True:
    display.show(image, loop=True, delay=200)
