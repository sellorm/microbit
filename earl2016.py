# EARL Banners and junk
# skip through options - lines on the the display, and choose one to select that message
# A Cycles through the options
# B selects that option. First press of B just plays that option once, the second puts it into an infinite loop
#
from microbit import Image, display, sleep, button_a, button_b

# set up opts and current positions
opt1 = Image('97531:00000:00000:00000:00000:')
opt2 = Image('00000:97531:00000:00000:00000:')
opt3 = Image('00000:00000:97531:00000:00000:')
opt4 = Image('00000:00000:00000:97531:00000:')
opt5 = Image('00000:00000:00000:00000:97531:')
opts = (opt1, opt2, opt3, opt4, opt5)
pos = 0
maxpos = len(opts) - 1

# I Love R
newi = Image('09990:00900:00900:00900:09990:')
clearimg = Image('00000:00000:00000:00000:00000:')
dotimg = Image('00000:00000:00900:00000:00000:')

def lover():
    display.show(newi)
    sleep(600)
    display.show(dotimg)
    sleep(200)
    display.show(Image.HEART_SMALL)
    sleep(200)
    display.show(Image.HEART)
    sleep(200)
    display.show(dotimg)
    sleep(200)
    display.show(Image.HEART_SMALL)
    sleep(200)
    display.show(Image.HEART)
    sleep(200)
    display.show(dotimg)
    sleep(200)
    display.show('R')
    sleep(600)
    display.show(clearimg)
    sleep(700)

# scroll: EARL 2016
def earlscroll():
    display.scroll('EARL 2016')

# scroll: #rstats
def rstats():
    display.scroll('#rstats ')
    
# rotateR stuffs
r45 = Image('90900:09090:00990:00900:00900:')
r90 = Image('99999:00909:00909:09090:90000:')
r135 = Image('00090:00900:99909:00990:00000:')
r180 = Image('90009:09009:00999:09009:00999:')
r225 = Image('00900:00900:99900:90900:09090:')
r270 = Image('00009:09090:90900:90900:99999:')
r315 = Image('00000:09900:90999:09000:00900:')

## set rotate delay
delay = 50

def rotater():
    display.show('R')
    sleep(delay*7)
    display.show(r45)
    sleep(delay)
    display.show(r90)
    sleep(delay)
    display.show(r135)
    sleep(delay)
    display.show(r180)
    sleep(delay)
    display.show(r225)
    sleep(delay)
    display.show(r270)
    sleep(delay)
    display.show(r315)
    sleep(delay)

# EARL Punchy
delay = 300
def punchy():
    display.show('E')
    sleep(delay)
    display.show('A')
    sleep(delay)
    display.show('R')
    sleep(delay)
    display.show('L')
    sleep(delay)
    display.show('2')
    sleep(delay)
    display.show('0')
    sleep(delay)
    display.show('1')
    sleep(delay)
    display.show('6')
    sleep(delay)
    display.show(' ')
    sleep(delay*3)

    
# Initialise
display.show(opts[pos])
# run
while True:
    if button_a.is_pressed():
        pos = pos + 1
        if (pos > maxpos):
            pos = 0
        display.show(opts[pos])
        sleep(300)
    if button_b.is_pressed():
        if(pos == 0):
            while True:
                lover()
                if button_a.was_pressed():
                    break
        elif (pos == 1):
            while True:
                earlscroll()
                if button_a.was_pressed():
                    break
        elif (pos == 2):
            while True:
                rstats()
                if button_a.was_pressed():
                    break
        elif (pos == 3):
            while True:
                rotater()
                if button_a.was_pressed():
                    break
        elif (pos == 4):
            while True:
                punchy()
                if button_a.was_pressed():
                    break
        display.show(opts[pos])
        sleep(300)
