# music player for all internal tunes
# button A - next tracks
# button B - play
# You must wait for a track to finish before trying to scroll through the tracks
from microbit import display, button_a, button_b, Image, sleep
import music

names = (
    ("Dadadadum", music.DADADADUM),
    ("Entertainer", music.ENTERTAINER),
    ("Prelude", music.PRELUDE),
    ("Ode", music.ODE),
    ("Nyan", music.NYAN),
    ("Ringtone", music.RINGTONE),
    ("Funk", music.FUNK),
    ("Blues", music.BLUES),
    ("Birthday", music.BIRTHDAY),
    ("Wedding", music.WEDDING),
    ("Funeral", music.FUNERAL),
    ("Punchline", music.PUNCHLINE),
    ("Python", music.PYTHON),
    ("Baddy", music.BADDY),
    ("Chase", music.CHASE),
    ("Ba Ding", music.BA_DING),
    ("Wawawawaa", music.WAWAWAWAA),
    ("Jump up", music.JUMP_UP),
    ("Jump down", music.JUMP_DOWN),
    ("Power up", music.POWER_UP),
    ("Power down", music.POWER_DOWN),
    )

# quaver fade
image = Image.MUSIC_QUAVER
image1 = image * 0.9
image2 = image * 0.8
image3 = image * 0.7
image4 = image * 0.6
image5 = image * 0.5
image6 = image * 0.4
image7 = image * 0.3
image8 = image * 0.2
fadeline = Image('00000:02000:10301:00020:00000:')
fade = [image, image1, image2, image3, image4, image5,
        image6, image7, image8, fadeline]
                
# sets params used for skipping through tracks
maxpos = len(names)-1
pos = 0

# startup
display.show(Image.ARROW_W)
sleep(1000)
display.scroll("skip")
display.show(Image.ARROW_E)
sleep(1000)
display.scroll("play")
display.show(fade, delay=100)
sleep(200)
display.scroll(names[pos][0])
display.show(fadeline)

# main
while True:
    if button_a.is_pressed():
        pos = pos + 1
        if (pos > maxpos):
            pos = 0
        display.scroll(names[pos][0])
        display.show(fadeline)
    if button_b.is_pressed():
        display.show(Image.MUSIC_QUAVER)
        music.play(names[pos][1])
        display.show(fade, delay=100)
