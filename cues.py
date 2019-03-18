import color_consts as cc
import utils as u
import LED_commands as lc
from time import sleep
import random as r

import serial as s


ser0 = s.Serial('/dev/ttyACM0', 9600)
ser1 = s.Serial('/dev/ttyACM1', 9600)
ser2 = s.Serial('/dev/ttyACM2', 9600)

def hydromatic():
    input("it's automatic...")
    u.sendRGB(ser0, 1, cc.RED)

    input("it's systematic...")
    u.sendRGB(ser1, 1, cc.RED)

    input("it's hydromatic...")
    u.sendRGB(ser0, 2, cc.ORANGE)
    u.sendRGB(ser1, 2, cc.ORANGE)

    input("it's greased lightning!...")
    lc.flash(ser0, 1, cc.RED, 1000, 200)
    lc.flash(ser1, 1, cc.RED, 1000, 200)
    sleep(1.1)
    lc.flash(ser0, 2, cc.ORANGE, 1000, 200)
    lc.flash(ser1, 2, cc.ORANGE, 1000, 200)

def magic_changes():
    input("c")
    u.sendRGB(ser0, 1, cc.RED)
    u.sendRGB(ser1, 1, cc.RED)

    input("a")
    u.sendRGB(ser0, 2, cc.BLUE)
    u.sendRGB(ser1, 2, cc.BLUE)

    input("f")
    u.sendRGB(ser0, 2, cc.RED)
    u.sendRGB(ser1, 2, cc.RED)

    input("g")
    u.sendRGB(ser0, 1, cc.BLUE)
    u.sendRGB(ser1, 1, cc.BLUE)

def beauty_school():
    input("start")
    u.sendRGB(ser0, 2, cc.PINK)
    u.sendRGB(ser1, 2, cc.PINK)

    input("nananananananana")
    u.sendRGB(ser2, 1, cc.LIGHT_BLUE)
    sleep(1.1)
    u.sendRGB(ser2, 2, cc.LIGHT_BLUE)

    input("stairs")
    u.sendRGB(ser0, 1, cc.PURPLE)
    u.sendRGB(ser1, 1, cc.PURPLE)

def freddy():
    input("half")
    u.sendRGB(ser0, 1, cc.PURPLE)
    u.sendRGB(ser1, 1, cc.PURPLE)

    input("full")
    u.sendRGB(ser0, 2, cc.PURPLE)
    u.sendRGB(ser1, 2, cc.PURPLE)

def hand_jive():
    input("go")
    lc.flash(ser0, 1, cc.RED, 1000, 1100)
    lc.flash(ser1, 2, cc.TURQUOISE, 1000, 1100)
    u.sendRGB(ser2, 1, cc.LIGHT_BLUE)
    sleep(1.2)
    lc.flash(ser0, 2, cc.LIME_GREEN, 1000, 1100)
    lc.flash(ser1, 1, cc.PURPLE, 1000, 1100)
    u.sendRGB(ser2, 2, cc.LIGHT_BLUE)


    input("repeat")
    lc.flash(ser0, 1, cc.RED, 1000, 1200)
    lc.flash(ser1, 2, cc.TURQUOISE, 1000, 1200)
    u.sendRGB(ser2, 1, cc.LIGHT_BLUE)
    sleep(1.2)
    lc.flash(ser0, 2, cc.LIME_GREEN, 1000, 1200)
    lc.flash(ser1, 1, cc.PURPLE, 1000, 1200)
    u.sendRGB(ser2, 2, cc.LIGHT_BLUE)


def animated():
    input("go")
    u.sendRGB(ser1, 1, cc.RED)
    sleep(1.2)
    u.sendRGB(ser1, 2, cc.ORANGE)
    sleep(1.2)
    u.sendRGB(ser2, 2, cc.YELLOW)
    sleep(1.2)
    u.sendRGB(ser2, 1, cc.GREEN)
    sleep(1.2)
    u.sendRGB(ser0, 2, cc.BLUE)
    sleep(1.2)
    u.sendRGB(ser0, 1, cc.PURPLE)

def solid():
    input("go")
    u.sendRGB(ser0, 2, cc.RED)
    u.sendRGB(ser2, 1, cc.TURQUOISE)
    sleep(1.1)
    u.sendRGB(ser1, 2, cc.RED)
    u.sendRGB(ser2, 2, cc.TURQUOISE)
    sleep(1.1)
    u.sendRGB(ser0, 1, cc.RED)
    u.sendRGB(ser1, 1, cc.RED)

def intermission():
    input("curtain")
    u.sendRGB(ser0, 2, cc.PURPLE)
    u.sendRGB(ser2, 1, cc.TURQUOISE)
    sleep(1.1)
    u.sendRGB(ser1, 2, cc.PURPLE)
    u.sendRGB(ser2, 2, cc.TURQUOISE)
    sleep(1.1)
    u.sendRGB(ser0, 1, cc.PURPLE)
    u.sendRGB(ser1, 1, cc.PURPLE)

    input("song on")
    lc.flash(ser0, 2, cc.RED, 1000, 500)
    lc.flash(ser1, 2, cc.RED, 1000, 500)
    sleep(1.1)
    lc.flash(ser0, 1, cc.PINK, 1000, 500)
    lc.flash(ser1, 1, cc.PINK, 1000, 500)
    sleep(1.1)
    u.sendRGB(ser2, 1, cc.TURQUOISE)
    u.sendRGB(ser2, 2, cc.TURQUOISE)

    input("song 2")
    lc.flash(ser0, 2, cc.BLUE, 1000, 500)
    lc.flash(ser1, 2, cc.BLUE, 1000, 500)
    sleep(1.1)
    lc.flash(ser0, 1, cc.PURPLE, 1000, 500)
    lc.flash(ser1, 1, cc.PURPLE, 1000, 500)
    sleep(1.1)
    u.sendRGB(ser2, 1, cc.TURQUOISE)
    u.sendRGB(ser2, 2, cc.TURQUOISE)


while True:
    print("Press 1: Hydromatic")
    print("Press 2: Magic Changes")
    print("Press 3: Beauty School")
    print("Press 4: Freddy My Love")
    print("Press 5: Hand Jive/We Go Together")
    print("6: Animated")
    print("7: Solids")
    print("8: Intermission")
    choice = int(input("Selection: "))

    if choice == 1:
        hydromatic()
    if choice == 2:
        magic_changes()
    if choice == 3:
        beauty_school()
    if choice == 4:
        freddy()
    if choice == 5:
        hand_jive()
    if choice == 6:
        animated()
    if choice == 7:
        solid()
    if choice == 8:
        intermission()
