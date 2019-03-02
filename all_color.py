import color_consts as cc
import utils as u
from time import sleep
import serial as s

ser0 = s.Serial('/dev/ttyACM0', 9600)
ser1 = s.Serial('/dev/ttyACM1', 9600)

def all_blue():
    input("go")
    u.sendRGB(ser0, 2, cc.LIGHT_BLUE)
    u.sendRGB(ser1, 2, cc.LIGHT_BLUE)
    sleep(1.1)
    u.sendRGB(ser0, 1, cc.LIGHT_BLUE)
    u.sendRGB(ser1, 1, cc.LIGHT_BLUE)

def all_red():
    input("go")
    u.sendRGB(ser0, 2, cc.RED)
    u.sendRGB(ser1, 2, cc.RED)
    sleep(1.1)
    u.sendRGB(ser0, 1, cc.RED)
    u.sendRGB(ser1, 1, cc.RED)

def all_green():
    input("go")
    u.sendRGB(ser0, 2, cc.GREEN)
    u.sendRGB(ser1, 2, cc.GREEN)
    sleep(1.1)
    u.sendRGB(ser0, 1, cc.GREEN)
    u.sendRGB(ser1, 1, cc.GREEN)

def all_purple():
    input("go")
    u.sendRGB(ser0, 2, cc.PURPLE)
    u.sendRGB(ser1, 2, cc.PURPLE)
    sleep(1.1)
    u.sendRGB(ser0, 1, cc.PURPLE)
    u.sendRGB(ser1, 1, cc.PURPLE)

def all_orange():
    input("go")
    u.sendRGB(ser0, 2, cc.RED_ORANGE)
    u.sendRGB(ser1, 2, cc.RED_ORANGE)
    sleep(1.1)
    u.sendRGB(ser0, 1, cc.RED_ORANGE)
    u.sendRGB(ser1, 1, cc.RED_ORANGE)

def all_off():
    input("go")
    u.sendRGB(ser0, 2, cc.OFF)
    u.sendRGB(ser1, 2, cc.OFF)
    sleep(1.1)
    u.sendRGB(ser0, 1, cc.OFF)
    u.sendRGB(ser1, 1, cc.OFF)

while True:
    print("Press 0: Off")
    print("Press 1: Blue")
    print("Press 2: Red")
    print("Press 3: Green")
    print("Press 4: Purple")
    print("Press 5: Orange")
    choice = int(input("Selection: "))

    if choice == 1:
        all_blue()
    if choice == 2:
        all_red()
    if choice == 3:
        all_green()
    if choice == 4:
        all_purple()
    if choice == 5:
        all_orange()
    if choice == 0:
        all_off()
