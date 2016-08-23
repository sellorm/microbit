# single LED fades in/out
#
from microbit import Image, display

image1 = Image('00000:00000:00900:00000:00000:')
image2 = image1 * 0.9
image3 = image1 * 0.8
image4 = image1 * 0.7
image5 = image1 * 0.6
image6 = image1 * 0.5
image7 = image1 * 0.4
image8 = image1 * 0.3
image9 = image1 * 0.2
image10 = image1 * 0.1
image11 = image1 * 0.0
image = (image1, image2, image3, image4, image5, image6, image7, image8,
         image9, image10, image11, image10, image9, image8, image7,
         image6, image6, image5, image4, image3, image2)

while True:
    display.show(image, loop=True, delay=50)
