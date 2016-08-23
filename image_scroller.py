# built-in image browser
# Button A scrolls backwards and button B forwards
#
from microbit import Image, display, button_a, button_b, sleep

names = [
    Image.HEART,
    Image.HEART_SMALL,
    Image.HAPPY,
    Image.SMILE,
    Image.SAD,
    Image.CONFUSED,
    Image.ANGRY,
    Image.ASLEEP,
    Image.SURPRISED,
    Image.SILLY,
    Image.FABULOUS,
    Image.MEH,
    Image.YES,
    Image.NO,
    Image.CLOCK1,
    Image.CLOCK2,
    Image.CLOCK3,
    Image.CLOCK4,
    Image.CLOCK5,
    Image.CLOCK6,
    Image.CLOCK7,
    Image.CLOCK8,
    Image.CLOCK9,
    Image.CLOCK10,
    Image.CLOCK11,
    Image.CLOCK12,
    Image.ARROW_N,
    Image.ARROW_NW,
    Image.ARROW_W,
    Image.ARROW_SW,
    Image.ARROW_S,
    Image.ARROW_SE,
    Image.ARROW_E,
    Image.ARROW_NE,
    Image.TRIANGLE,
    Image.TRIANGLE_LEFT,
    Image.CHESSBOARD,
    Image.DIAMOND,
    Image.DIAMOND_SMALL,
    Image.SQUARE,
    Image.SQUARE_SMALL,
    Image.RABBIT,
    Image.COW,
    Image.MUSIC_CROTCHET,
    Image.MUSIC_QUAVER,
    Image.MUSIC_QUAVERS,
    Image.PITCHFORK,
    Image.XMAS,
    Image.PACMAN,
    Image.TARGET,
    Image.TSHIRT,
    Image.ROLLERSKATE,
    Image.DUCK,
    Image.HOUSE,
    Image.TORTOISE,
    Image.BUTTERFLY,
    Image.STICKFIGURE,
    Image.GHOST,
    Image.SWORD,
    Image.GIRAFFE,
    Image.SKULL,
    Image.UMBRELLA,
    Image.SNAKE,
    Image.ALL_CLOCKS,
    Image.ALL_ARROWS,
    ]

maxpos = len(names)-1
pos = 0
display.show(names[pos])

while True:
    if button_a.is_pressed():
        pos = pos - 1
        if (pos < 0):
            pos = maxpos
        display.show(names[pos])
        sleep(500)
    if button_b.is_pressed():
        pos = pos + 1
        if (pos > maxpos):
            pos = 0
        display.show(names[pos])
        sleep(500)
